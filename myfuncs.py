#!/bin/python
# -*-coding:gbk-*-

def chinese2digits(uchars_chinese):
	common_used_numerals = {
						u'零':0, u'一':1, u'二':2, u'三':3, u'四':4, u'五':5, u'六':6, u'七':7, 
						u'八':8, u'九':9, u'十':10, u'百':100, u'千':1000, u'万':10000, u'亿':100000000 }
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
