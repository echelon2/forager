
# Python libs 
import requests
from lxml import etree
from lxml.cssselect import CSSSelector
from lxml.etree import fromstring
from StringIO import StringIO

# Our libraries
from url import Url

class Document(object):

	def __init__(self, url=None):

		if type(url) is str:
			url = Url(url)
		elif type(url) is not Url:
			raise Exception, 'Must supply Url object to Document.'

		self.url = url
		self.title = None		# Parsed out html title
		self.httpStatus = None	# HTTP status code
		self.mimeType = None	# Document type (html, jpeg, css, etc.)
		self.depth = -1			# Simple depth of the page from root doc

		self.requested = False	# If the page has been requested

		self._cachedRequest = None # Cached requests object 
		self._cachedLinks = [] # Cached links extracted from HTML

		self.linksIn = []
		self.linksOut = []

	def download(self):
		if self.requested:
			return

		self.requested = True

		def parseMime(ct):
			"""
			Simplify/extract mimetype.
			"""
			if 'text/html' in ct:
				return 'text/html'
			return ct

		try:
			r = requests.get(self.url)
			self.httpStatus = r.status_code
			self.mimeType = parseMime(r.headers['content-type'])
			self._cachedRequest = r # Cache requests object (for now)
		except KeyboardInterrupt:
			raise KeyboardInterrupt

		#except:
		#	self.httpStatus = 0

	def isMissing(self):
		"""
		If the HTTP status code is 404, the page is missing.
		In the future, we'll consider other error codes and timeouts.
		"""
		return self.httpStatus in [0, 404]

	def getUrls(self):
		"""
		Get all of the URLs in the HTML document.
		If the page didn't download, we return an empty list.
		The results are cached.
		WORK IN PROGRESS
		"""
		if self._cachedLinks:
			return self._cachedLinks

		if self.isMissing():
			return []

		# TODO: Make a set rather than list to provide uniquenes
		extracted = []

		try:
			domRoot = etree.parse(
					StringIO(self._cachedRequest.content),
					etree.HTMLParser()).getroot()

			selector = CSSSelector('a')
			links = []
			for el in selector(domRoot):
				if 'href' not in el.attrib:
					continue

				href = el.attrib['href']

				# TODO: HANDLE REL LINKS
				if href[0:4].lower() != 'http':
					continue

				url = Url(href, self.url)
				links.append(url)

			extracted.extend(links)

		except KeyboardInterrupt:
			raise KeyboardInterrupt

		except:
			# FIXME: Better error handling
			print "Exception in DOM parsing"

		self._cachedLinks = extracted
		return extracted

"""
THIS IS TEST CODE --
IT'LL ONLY RUN IF THIS FILE IS EXECUTED DIRECTLY.
"""
if __name__ == '__main__':
	#try:
	p = Document('http://spsu.edu')
	p.download()
	p.getUrls()
	for url in p.getUrls():
		print "url: %s" % url

	#except:
	#	print "Exception occurred"

