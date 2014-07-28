#!/usr/bin/python

from bs4 import BeautifulSoup

input_file = "index.html"
html_doc = open(input_file)
soup = BeautifulSoup(html_doc)

for entry in soup.find_all('li'):
	print entry.a.string.strip()
	print ">> " + entry.a['href']


