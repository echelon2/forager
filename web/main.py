#!/usr/bin/env python 
"""
This is the flask website that powers report viewing.
"""

# Python libs
import random
from flask import Flask
from flask import render_template

# Our code
from database import ALL_PAGES, MISSING_PAGES
from document import Document
from url import Url

app = Flask(__name__)

@app.route('/')
def page_index():
	global ALL_PAGES
	global MISSING_PAGES

	print len(ALL_PAGES)
	print len(MISSING_PAGES)

	return render_template('index.html', all=ALL_PAGES, missing=MISSING_PAGES)

@app.route('/url/<urlId>')
@app.route('/url/<urlId>/')
def page_report(urlId):
	global ALL_PAGES

	urlId = int(urlId)

	doc = ALL_PAGES[urlId]

	return render_template('url.html', doc=doc)


if __name__ == "__main__":
    app.run()
