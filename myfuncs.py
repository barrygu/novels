#!/bin/python
# -*-coding:gbk-*-

def chinese2digits(uchars_chinese):
	common_used_numerals = {
						u'��':0, u'һ':1, u'��':2, u'��':3, u'��':4, u'��':5, u'��':6, u'��':7, 
						u'��':8, u'��':9, u'ʮ':10, u'��':100, u'ǧ':1000, u'��':10000, u'��':100000000 }
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
