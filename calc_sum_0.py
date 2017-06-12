#!/usr/bin/env python
#-*- coding: utf-8 -*-

def calc_sum(*args):
	ax = 0 
	for n in args:
		ax = ax + n 
	return ax

y = calc_sum(1,2,3,4,5)

print y 
