# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:53:41 2014

@author: sawyer
"""

def grid(n):
    print '+'+n*(4*' -'+' +')
    print n*(4*('|'+n*(9*' '+'|')+'\n')+'+'+n*(4*' -'+' +')+'\n')
    
grid(4)