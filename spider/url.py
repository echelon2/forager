"""
This module presents URL-parsing logic.
It should be able to manipulate relative and absolute URIs,
join basenames, etc.
"""

# Python stdlib
import urlparse

class Url(str):
	"""
	We normally don't subclass immutable strings, but we're using string
	semantics and adding new functionality.
	"""

	def __new__(self, url, base=None):
		"""
		Here we join the baseUrl to the path if it's a relative url.
		New is not a CTOR! New is an instance factory that fires before
		the CTOR runs.
		"""
		absUrl = url if not base else urlparse.urljoin(base, url)
		return str.__new__(self, absUrl)

# TEST CODE
if __name__ == '__main__':
	u = Url("http://google.com")
	print u

	u = Url('../some/directory/file.gif',
			'http://spsu.edu/cse/faculty')
	print u

	u = Url('http://google.com/some/directory/file.gif',
			'http://spsu.edu/cse/faculty')
	print u


