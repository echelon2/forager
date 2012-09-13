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

urls = ['http://spsu.edu', 'http://google.com','http://baidu.com','http://sadsafioasf.com']

for url in urls:
    p = Page(url)
    p.request() # Does the request.
 
    print "Is page missing? %s" % str(p.isMissing())
"""
All_Documents = {}
Unvisited_Queue = []
Unvisited_Queue.append("http://spsu.edu")

while len(Unvisited_Queue) > 0:
    url = Unvisited_Queue.pop(0)
    print url
    
    p=Document(url)
    p.download()
    All_Documents[url]=p
    urls = p.getUrls()
    print urls
    for u in urls:
        if u not in All_Documents:
            Unvisited_Queue.append(u)
            
