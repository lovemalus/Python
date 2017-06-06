#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math 

L = range(0,101)

def isprime2(n):
	if n<= 1:
		return True
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0:
			return True
	
	return False

y = filter(isprime2, L )

print y