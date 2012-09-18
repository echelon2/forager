#!/usr/bin/env python

# Python libs
import requests
from Queue import PriorityQueue

# Our code
from document import Document
from url import Url

"""
CONFIGURATION
"""

ROOT_URL = Url('http://spsu.edu')


"""
DATA STRUCTURES
Some small data structures.
"""

class RequestQueue(PriorityQueue):

	def push(self, url, priority=1000):
		"""Push a url onto the queue."""
		self.put_nowait((priority, url))

	def pop(self):
		"""Pop an item from the queue."""
		item = self.get()
		return item[0] if len(item) == 1 else item[1]


class Database(dict):

	def addUrl(self, url):
		if url not in self:
			self[url] = Document(url)


"""
GLOBALS
Some global vars for bookkeeping.
"""

# Database (dictionary of url->document) of all pages
DB = {}

# Ongoing requests
RQ = RequestQueue()

"""
MAIN
Main code.
"""

def main(url):
	global DB
	global RQ

	#if type(url) == str:
	#	url = Url(url)

	RQ.push(url)
	DB[url] = Document(url)

	while not RQ.empty():
		url = RQ.pop()
		doc = None

		# Database entry
		if url in DB:
			doc = DB[url]
		else:
			doc = Document(url)
			DB[url] = doc

		if doc.requested:
			continue

		print "Downloading %s" % url
		doc.download()

		urls = doc.getUrls()
		for u in urls:
			if u not in DB:
				DB[u] = Document(u)
				RQ.push(u, 1)
			elif DB[u].requested:
				RQ.push(u, 1) # XXX: Raise priority

main(ROOT_URL)


