#!/bin/python
# -*-coding:gbk-*-

import os, re
import httplib
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

class ListParser(SGMLParser):
	get_start = False
	href = None

	def handle_data(self, data):
		txt = data.strip()
		if self.get_start == True and self.href and txt:
			print '%s %s' % (self.href, txt)
			self.href = None

	def start_a(self,attrs):
		if self.get_start == True:
			for k, v in attrs:
				if k == 'href':
					self.href = v
					break

	def start_table(self,attrs):
		return

	def end_table(self):
		if self.get_start == True:
			self.get_start = False

	def start_div(self,attrs):
		if not self.get_start:
			for k, v in attrs:
				if k == 'id' and re.match('defaulthtml', v.strip(), re.I):
					self.get_start = True
					break

ListParser().feed(data)
