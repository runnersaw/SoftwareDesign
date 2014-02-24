# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:12:02 2014

@author: sawyer
"""

import random

def get_complementary_base(n):
    """ You thought this would be helpful documentary
    
    You were wrong."""
    if n== 'a':
        return 't'
    elif n== 't':
        return 'a'
    elif n== 'c':
        return 'g'
    elif n== 'g':
        return 'c'
    elif n== 'A':
        return 'T'
    elif n== 'T':
        return 'A'
    elif n== 'C':
        return 'G'
    elif n== 'G':
        return 'C'
    else:
        return 'ERROR ERROR ERROR ERROR ERROR ERROR ERROR'
        
print get_complementary_base(3)

def is_between(x,y,z):
    print y>=x and y<=z
    
is_between(2,4,4)

def random_float(start,stop):
    print start + (stop-start)*random.random()
    
help(get_complementary_base)
    
random_float(2,63)

def factorial(n):
    s=1
    for i in range(n):
        s=s*(i+1)
    print s
        
factorial(5)
    
    
    