#!/bin/python
# -*-coding:gbk-*-

import os, sys
import httplib
import myfuncs
from sgmllib import SGMLParser

fname = "chapters.html"

if os.path.exists(fname):
	afile = open(fname, 'r')
	data = afile.read()
	afile.close()
else:
	conn = httplib.HTTPConnection("www.lwxs.org")
	conn.request("GET", "/books/2/2754/index.html")
	resp = conn.getresponse()
	if resp.status == 200:
		data = resp.read()
		afile = open(fname, 'w')
		afile.write(data)
		afile.close()
	resp.close()
	conn.close()

t = myfuncs.chinese2digits(u'五百六十七')
print t

tagstack = []
class ShowStructure(SGMLParser):
	def handle_starttag(self, tag, method,attrs): 
		tagstack.append(tag)
	def handle_endtag(self, tag): tagstack.pop()  
	def handle_data(self, data):  
		if data.strip():
			for tag in tagstack: sys.stdout.write('/'+tag)  
			sys.stdout.write(' >> %s\n' % data.strip().decode('gbk').encode('utf8'))  

	def unknown_starttag(self,tag,attrs):  
		print 'start tag:<'+tag+'>'  
		#if len ( attrs ):
		#	print "=====> %s\n" % str( attrs )
		if tag == 'div':
			for item in attrs: 
				if item[0] == "id" and item[1] == "container_bookinfo": 
					print "=====> %s\n" % str( attrs )
	def unknown_endtag(self,tag):  
		print 'end tag:</'+tag+'>'  
	def start_lala(self,attr):  
		print 'lala tag found'  

ShowStructure().feed(data)