#!/usr/bin/env python

"""
from ghost import Ghost

ghost = Ghost()

page, res = ghost.open("http://www.spsu.edu")

print page
print res
"""

import requests

r = requests.get("http://www.spsu.edu")

print r
print dir(r)
print r.content
