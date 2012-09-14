
# Python standard library
from StringIO import StringIO

# Additional Python Libraries
import requests
from lxml import etree
from lxml.cssselect import CSSSelector
from lxml.etree import fromstring

class Document(object):

	def __init__(self, url=None):

		self.url = url
		self.title = None	 # Parsed out html title
		self.httpCode = None # HTTP status code
		self.mimeType = None # Document type (html, jpeg, css, etc.)

		self.downloaded = False # If the page has been requested

		self._cachedRequest = None # Cached requests object 
		self._cachedLinks = [] # Cached links extracted from HTML

	def download(self):
		if self.downloaded:
			return
		self.downloaded = True

		try:
			r = requests.get(self.url)
			self.httpCode = r.status_code
			self.mimeType = r.headers['content-type']
			self._cachedRequest = r # Cache requests object (for now)
		except:
			self.httpCode = 0

	def isMissing(self):
		"""
		If the HTTP status code is 404, the page is missing.
		In the future, we'll consider other error codes and timeouts.
		"""
		return self.httpCode is 404 or self.httpCode is 0

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

				links.append(href)

			extracted.extend(links)

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

