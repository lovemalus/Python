#!/usr/bin/env python
#-*- coding: utf-8 -*-
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'begin call %s():' % func.__name__
		func(*args,**kw)
		print 'end call'
	return wrapper


@log
def now():
	print '测试装饰器'

now()