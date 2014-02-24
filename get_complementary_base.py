# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:12:02 2014

@author: sawyer
"""

def get_complementary_base(n):
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

