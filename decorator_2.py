#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():'%(text,func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print '2017-06-21'

now()

