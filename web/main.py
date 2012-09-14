#!/usr/bin/env python 
"""
This is the flask website that powers report viewing.
"""

import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	"""
	This is the root page.
	See the @app.route("/") decarator?
	Flask is awesome.
	"""

	simpleHtml = """
	<h1>This is an example page</h1>
	<hr>
	<ul>
		<li><a href="/mark">Mark's page</a></li>
		<li><a href="/brandon">Brandon's page</a></li>
		<li><a href="/sha">Sha's page</a></li>
		<li><a href="/something">Something!?</a></li>
	</ul>
"""

	return simpleHtml

@app.route("/mark")
def mark():
	return "This is Mark's page. Mark likes donuts."

@app.route("/brandon")
def brandon():
	num = random.randint(1, 10)
	return "This is Brandon's page. He likes the number %d." % num


@app.route("/sha")
def sha():
	colors = ['pink', 'red', 'green', 'blue', 'yellow']
	color = colors[random.randint(0, len(colors))]
	return "This is Sha's page. She likes the color %s." % color

if __name__ == "__main__":
    app.run()
