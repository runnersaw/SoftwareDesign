# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:23:33 2014

@author: sawyer
"""

from math import *

def Ackermann(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return Ackermann(m-1, 1)
    else:
        return Ackermann(m-1, Ackermann(m, n-1))
    
def estimate_pi():
    k=0.0
    estimate = 0.0
    running = True
    while running:
        term1 = factorial(4.0*k)
        print term1
        term2 = (1103.0+26390.0*k)
        print term2
        term3 = (factorial(k))**4.0
        print term3
        term4 = 396.0**(4.0*k)
        print term4
        term5 = 2.0*sqrt(2.0)/9801.0
        print term5
        thing = term1*term2/term3/term4*term5
        print thing
        add_pi = 1.0/thing
        print add_pi
        estimate += add_pi
        print estimate
        k+=1.0
        if estimate > 100000:
            break
        if add_pi < 1e-15:
            running = False
        
    
    
if __name__ == '__main__':
    print Ackermann(3,4)
    print estimate_pi()
            