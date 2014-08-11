#!/bin/python
# -*-coding:gbk-*-

import os, re
import httplib

fname = "chapters.html"

def chinese2digits(uchars_chinese):
	common_used_numerals = {u'零':0, u'一':1, u'二':2, u'三':3, u'四':4, u'五':5, u'六':6, u'七':7, u'八':8, u'九':9, u'十':10, u'百':100, u'千':1000, u'万':10000, u'亿':100000000}
	total = 0
	r = 1

	for i in range(len(uchars_chinese) - 1, -1, -1):
		x = common_used_numerals.get(uchars_chinese[i], 0)
		if x >= 10:
			if x > r:
				r = x
			else:
				r = r * x
			if i == 0:
				total += r
		else:
			total += r * x

	return total

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

regexp = "<TD class=bookinfo_td .*>"
pattern = re.compile(regexp, re.I)
result = re.split(pattern, data)

regexp = "<\/TABLE>"
pattern = re.compile(regexp, re.I)
result = re.split(pattern, result[1])

regexp = "<a .*href\s*=.*<\/a>"
pattern = re.compile(regexp, re.I)

afile = open("chapters.lst", 'w')
bfile = open("chapters.txt", 'w')

p = re.compile(ur'href=["\'](?P<href>[^"\']*)["\'].*>(?P<title>.*)<', re.I)
p3 = re.compile(ur'第(.*)章\s')
# p3 = re.compile(u'\u7b2c(.*)\u7ae0\s')
for item in pattern.finditer(result[0]):
	txt = item.group()
	afile.write("%s\n" % txt)

	txt = txt.decode('gbk')  # convert to unicode

	m = p.search(txt)
	t1 = m.group('href')
	t2 = m.group('title')

	t = (t1.encode('gbk'), t2.encode('gbk'))
	bfile.write("%s %s\n" % t)

	m = p3.search(t2)
	if m:
		t = chinese2digits(m.group(1))
		print m.group(), t

bfile.close()
afile.close()
