#!/usr/bin/env python

# Python libs
import sys
import requests
import pickle
import copy
from Queue import PriorityQueue
from datetime import datetime

# Our code
import pypath
from document import Document
from url import Url

"""
CONFIGURATION
"""

ROOT_URL = Url('http://spsu.edu')
SAVE_EVERY = 7

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
Misc functions
"""

def save(obj, filename):
	print "Saving file: %s" % filename
	pickle.dump(obj, open(filename, 'wb'))

def save_database():
	global DB
	fn = str(datetime.now()).replace(' ', '_')
	save(DB, '../cache/db_' + fn + '.obj')

def save_queue():
	global RQ
	# Can't pickle queue
	queue = copy.copy(RQ) # XXX: Still not working
	li = []
	while not queue.empty():
		li.append(queue.get_nowait())

	fn = str(datetime.now()).replace(' ', '_')
	save(li, '../cache/queue_' + fn + '.obj')

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

	doc = Document(url)
	RQ.push(doc)
	#DB[url] = Document(url)

	try:
		count = 0
		while not RQ.empty():
			doc = RQ.pop()
			url = doc.url

			print "Url '%s' dequeued." % doc.url

			# Don't fetch again if in database.
			if doc.url in DB:
				continue

			DB[url] = doc

			print "Downloading..."
			doc.download()

			# If we just downloaded an external domain, we 
			# don't continue to spider it.
			if not url.isOnDomain('spsu.edu'):
				continue

			if doc.isMissing():
				continue

			urls = doc.getUrls()
			print "%d urls parsed from page" % len(urls)

			for u in urls:
				if u not in DB:
					d = Document(u)
					d.linksIn.append(doc)
					RQ.push(d, 1) # TODO: priority heuristic
				else:
					d = DB[u]
					d.linksIn.append(doc)

				doc.linksOut.append(d)

			count += 1
			if count % SAVE_EVERY == 0:
				save_database()
				count = 1

	except KeyboardInterrupt:
		sys.exit()
		print "Keybord Interrupt, spider terminating."
		save_queue() # XXX This should be fixed.
		return

	except Exception as e:
		import sys, traceback
		print '\n---------------------'
		print "Exception occurred in mainloop"
		print 'Exception: %s' % e
		print '- - - - - - - - - - -'
		traceback.print_tb(sys.exc_info()[2])
		print "\n"
		pass

main(ROOT_URL)


