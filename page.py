
# Additional Python Libraries
import requests

class Page(object):

	def __init__(self, url=None):

		self.url = url
		self.title = None	 # Parsed out html title
		self.httpCode = None # HTTP status code
		self.mimeType = None # Document type (html, jpeg, css, etc.)

		self._request = None # Requests object wrapper
		self.fetched = False # If the page has been requested


	def request(self):
		if self.fetched:
			return

		r = requests.get("http://www.spsu.edu")
		self.httpCode = r.status_code
		self.mimeType = r.headers['content-type']
		self._request = r # Cache requests object (for now)

	def isMissing(self):
		"""
		If the HTTP status code is 404, the page is missing.
		In the future, we'll consider other error codes and timeouts.
		"""
		return self.httpCode is 404

