#!/usr/bin/env python 

"""
This is the flask website that powers report viewing.
"""

# Python libs
import os
import glob
import random
from flask import Flask
from flask import render_template

# Our code
import pypath
import pickle
#from database import ALL_PAGES, MISSING_PAGES
from document import Document
from url import Url


"""
THIS IS REALLY MESSY INTEGRATION!
The reports are compiled here.
Bad Brandon! Bad!
"""

CACHE_DIR = '../cache'
dirfiles = glob.glob(CACHE_DIR + '/*obj')
dirfiles.sort()

DATABASE_FILE = dirfiles[-2]

f = open(DATABASE_FILE)
db = pickle.loads(f.read())

pagelist = []
i = 0
for url, doc in db.iteritems():
	doc.cacheId = i
	pagelist.append(doc)
	i+= 1

ALL_PAGES = tuple(pagelist)

errlist = []
for doc in ALL_PAGES:
	if doc.isMissing():
		errlist.append(doc)

# Generate page statistics
for doc in ALL_PAGES:
	outBad = 0
	for d in doc.linksOut:
		if d.isMissing():
			outBad += 1
	doc.cacheOutBad = outBad

MISSING_PAGES = tuple(errlist)

"""
FLASK APP.
Flask rocks for fast web backend dev.
"""

app = Flask(__name__)

@app.route('/')
def page_index():
	global ALL_PAGES, MISSING_PAGES
	return render_template('index.html', all=ALL_PAGES, missing=MISSING_PAGES)

@app.route('/url/<urlId>')
@app.route('/url/<urlId>/')
def page_report(urlId):
	global ALL_PAGES
	return render_template('url.html', doc=ALL_PAGES[int(urlId)])

if __name__ == "__main__":
    app.run()
