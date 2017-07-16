#!/usr/bin/env python
#-*- coding: utf-8 -*-

import functools


def log(func):
	 @functools.wraps(func)
	 def wrape(*args,**kw):
	 	print 'begin call'
	 	func(*args,**kw)
	 	print 'end call'
	 	return 

	 return wrape

@log
def now():
	print '2017年7月10日09:50:45'

now()