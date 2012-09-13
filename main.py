#!/usr/bin/env python

"""
from ghost import Ghost

ghost = Ghost()

page, res = ghost.open("http://www.spsu.edu")

print page
print res
"""

# Python Standard Library
# (None yet)

# Additional Python Libraries
import requests

# Our code
from page import *

"""
r = requests.get("http://www.spsu.edu")
print r
print dir(r)
print r.content
print "I edited this file"
print "Brandon edited it too! Git is working :)"
"""

p = Page("http://www.spsu.edu")
p.request() # Does the request.

print dir(p._request)
print "Is page missing? %s" % str(p.isMissing())

