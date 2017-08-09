#! usr/bin/env python 
# -*- coding:utf-8 -*-

import os

os.chdir(r'D:\depot\Git')

print u'当前目录: %s' % os.getcwd()
print u'当前目录的文件: %s' % os.listdir(r'D:\depot\Git')

'''
     在windows的cmd 控制台中文件的编码方式是gbk编码方式，所以使用cmd运行文件的时候，必须在文件
	的开头注释上utf-8的编码方式，并在print中出现中文的时候使用
	print u'中文' 的格式
    但使用shell和其他解释器中则不需要在开头和print中加入该注释，可以直接读取。
	注释有三种方式
	1、#
	2、'''  '''
	3、"""  """
'''
