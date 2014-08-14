#!/bin/python
# -*-coding:gbk-*-

import os, re
import myfuncs

fname = "chapters.html"

if os.path.exists(fname):
	afile = open(fname, 'r')
	data = afile.read()
	afile.close()
else:
	data = myfuncs.get_page('http://www.lwxs.org/books/2/2754/index.html')
	myfuncs.save_file(fname, data)

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
		t = myfuncs.chinese2digits(m.group(1))
		print m.group(), t

bfile.close()
afile.close()
