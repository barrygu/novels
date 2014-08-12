#!/bin/python
# -*-coding:gbk-*-

import os #, sys
import httplib
#import myfuncs
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

#t = myfuncs.chinese2digits(u'五百六十七')
#print t

#tagstack = []
list_pairs=[]
class ShowStructure(SGMLParser):
	get_start = False
	href=None
	#def handle_starttag(self, tag, method,attrs): 
	#	tagstack.append(tag)
	#def handle_endtag(self, tag, method): 
	#	tagstack.pop()
	def handle_data(self, data):
		txt = data.strip()
		if self.get_start == True and self.href and txt:
			#for tag in tagstack: sys.stdout.write('</'+tag)
			#sys.stdout.write(' >> %s\n' % data.strip()) #.decode('gbk').encode('utf8'))
			list_pairs.append( (self.href, txt) )
			self.href = None
	#def unknown_starttag(self,tag,attrs):  
	#	print 'start tag:<'+tag+'>'  
	#def unknown_endtag(self,tag):  
	#	print 'end tag:</'+tag+'>'  
	#def start_lala(self,attr):  
	#	print 'lala tag found'  

	def start_a(self,attrs):
		if self.get_start == True:
			#attr_href = [v for k, v in attrs if k=='href']
			#if attr_href: 
			#	self.href = attr_href[0]
			for k, v in attrs:
				if k == 'href':
					self.href = v

	def start_table(self,attrs):
		return 0

	def end_table(self):
		if self.get_start == True:
			self.get_start = False

	def start_div(self,attrs):
		if not self.get_start:
			#attr_id = [v for k, v in attrs if k=='id']
			#if attr_id and attr_id[0].lower() == 'defaulthtml': #'container_bookinfo':
			#	self.get_start = True
			for k, v in attrs:
				if k == 'id' and v.lower() == 'defaulthtml':
					self.get_start = True

ShowStructure().feed(data)
for item in list_pairs:
	print '%s %s' % item
