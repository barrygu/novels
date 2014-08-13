#!/bin/python
# -*-coding:gbk-*-

import os, re, sys
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
		if self.href and txt:
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

class ContentParser(SGMLParser):
	get_start = False
	pre_data = False
	
	def start_div(self,attrs):
		if not self.get_start:
			for k, v in attrs:
				if k == 'id' and re.match('content', v.strip(), re.I):
					self.get_start = True
					break

	def start_p(self,attrs):
		if self.get_start:
			self.pre_data = True

	def end_p(self):
		if self.pre_data:
			self.pre_data = False

	def handle_entityref(self, name):
		if name == 'nbsp':
			sys.stdout.write(' ')
		
	def handle_data(self, data):
		txt = data.strip()
		if self.pre_data and txt:
			print '%s' % (txt)

fname = "524186.html"

if os.path.exists(fname):
	afile = open(fname, 'r')
	data = afile.read()
	afile.close()
else:
	conn = httplib.HTTPConnection("www.lwxs.org")
	conn.request("GET", "/books/2/2754/524186.html")
	resp = conn.getresponse()
	if resp.status == 200:
		data = resp.read()
		afile = open(fname, 'w')
		afile.write(data)
		afile.close()
	resp.close()
	conn.close()

ContentParser().feed(data)
