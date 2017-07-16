#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import functools
def log(text):
    if isinstance(text,str):                                        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):                   
                if text:                    
                    print'%s %s(): '%(text,func.__name__)
                else:                    
                    print'call %s(): '% func.__name__
                func(*args,**kw)        
                return                    
            return wrapper                 
        return decorator                
    else:
        @functools.wraps(text)            
        def wrapper(*args,**kw):           
            print'call %s(): '%text.__name__
            text(*args,**kw)            
            return
        return wrapper
 
@log
def f1():
    print 'testing1'
 
@log('')
def f2():
    print 'testing2'
 
@log('excute')
def f3():
    print 'testing3'

f1()
f2()
f3()
