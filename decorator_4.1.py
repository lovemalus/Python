#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import functools
def log(obj):
    if isinstance(obj,str):        #判断参数obj是否为字符串，若不是，则其为函数参数，执行else内容
                                #若是字符串，说明其为带参数的decorator
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('begin call')        #打印函数开始执行信息
                if obj:                    #如果字符串不为空
                    print('%s %s(): '%(obj,func.__name__))
                else:                    #字符串为空时
                    print('call %s(): '% func.__name__)
                func(*args,**kw)        #不使用return来返回函数func，而是直接执行，这样可以在该句后面再打印信息
                print('end call')        #打印函数执行结束信息
                return                    # wrapper函数的返回
            return wrapper                 #decorator函数的返回
        return decorator                #log函数的返回
    else:
        @functools.wraps(obj)            #obj即为函数名称
        def wrapper(*args,**kw):
            print('begin call')
            print('call %s(): '%obj.__name__)
            obj(*args,**kw)
            print('end call')
            return
        return wrapper
 
@log
def fnc():
    print('I\'m fnc for testing log without parameter')
 
@log('')
def fnc2():
    print('I\'m fnc2 for testing log with empty parameter')
 
@log('excute')
def fnc3():
     print('I\'m fnc3 for testing log with parameter')
 
fnc()
print('fnc.__name__ = %s' % fnc.__name__)
print('----------------------------------')
fnc2()
print('fnc2.__name__ = %s' % fnc2.__name__)
print('----------------------------------')
fnc3()
print('fnc3.__name__ = %s' % fnc3.__name__)