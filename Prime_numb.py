#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math 

L = range(0,101)

def isprime1(n):
	if n<= 1:
		return False
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	
	return True 

y = filter(isprime1, L )

print y


