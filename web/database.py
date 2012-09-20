from url import Url
from document import Document

"""
Globals to export
"""

MISSING_PAGES = ()
ALL_PAGES = ()

"""
Throw together a toy/example database of urls.
"""

urls = [
	'http://spsu.edu',
	'http://cse.spsu.edu',
	'http://swe.spsu.edu',
	'http://library.spsu.edu',
]

missing = [
	'http://adfasfasf.com',
	'http://foo.com/asdfasdf/wh2hjdhdf/',
	'http://google.com/notarealpage/',
	'http://kahsdfhasdhfjkahsf.net',
]

urls = [Document(u) for u in urls]
missing = [Document(u) for u in missing]

allp = []
allp.extend(urls)
allp.extend(missing)

for d in urls:
	d.requested = True
	d.httpStatus = 200

for d in missing:
	d.requested = True
	d.httpStatus = 404

def make_link(a, b):
	if a.isMissing():
		return
	a.linksOut.append(b)
	b.linksIn.append(a)

make_link(urls[0], urls[1])
make_link(urls[0], urls[2])
make_link(urls[0], urls[3])

make_link(urls[1], urls[0])
make_link(urls[1], urls[2])
make_link(urls[1], urls[3])

make_link(urls[2], urls[3])

make_link(urls[0], missing[0])
make_link(urls[1], missing[0])
make_link(urls[1], missing[2])
make_link(urls[2], missing[1])
make_link(urls[2], missing[2])
make_link(urls[2], missing[3])

"""
Here are the final database objects.
"""

MISSING_PAGES = tuple(allp)
ALL_PAGES = tuple(allp)

