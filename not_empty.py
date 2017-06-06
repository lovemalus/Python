#!/usr/bin/python
# -*- coding: UTF-8 -*-

def not_empty(s):
	return s and s.strip()

y = filter(not_empty, ['A', '', 'B', None, 'C', '  '])

print y
