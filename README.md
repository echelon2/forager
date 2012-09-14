Forager
=======

Forager is a webcrawler for the spsu.edu domain that finds and 
generates web reports on missing media files and hyperlinks 
throughout the website.

This is the readme file for the project.
We will update it with more documentation as it becomes 
available.

Required Python Libraries
-------------------------
* **flask** -- excellent, lightweight web platform
* **lxml** -- provides HTML parsing
* **requests** -- performs HTTP 

These can be installed on Linux or Windows with `pip`, 
the Python package manager, eg: 

`pip install flask`
`pip install lxml`
`pip install requests`

To install lxml on Windows, you'll need the libxml2 and libxslt. 
The easiest way to fix this is to simply use the precompiled 
lxml found here:

* [Precompiled extensions for Windows](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

