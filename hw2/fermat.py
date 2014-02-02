# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:00:44 2014

@author: sawyer
"""

def check_fermat(a,b,c,n):
    if n>2:
        if a**n + b**n == c**n:
            print 'Holy smokes, Fermat was wrong!'
        else:
            print 'Fermat was right'
    else:
        print 'Fermat was right'

def check_fermat2():
    x=raw_input('Give me an integer ')
    y=raw_input('Give me an integer ')
    z=raw_input('Give me an integer ')
    n=raw_input('Give me an integer ')
    x=int(x)
    y=int(y)
    z=int(z)
    n=int(n)
    check_fermat(x,y,z,n)
    
check_fermat2()