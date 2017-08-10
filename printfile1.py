# printfile1.py
from __future__ import print_function

def print_file1(fname):
    f = open(fname,'r')
    for line in f:
        print (line, end= '')

print (print_file1(r'C:\Users\lenovo\Documents\GitHub\Python\forsum.py'))
