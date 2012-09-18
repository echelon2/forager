#!/usr/bin/env python

# Python Standard Library
# (None yet)

# Additional Python Libraries
import requests

# Our code
from document import *

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

