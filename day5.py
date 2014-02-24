# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:27:19 2014

@author: sawyer
"""

from random import randint

def hinge(n):
    if n < 0:
        return 0
    else:
        return n
        
def print_number_of_days(n):
    if n == 1:
        print 'Input is 1 day'
    else:
        print 'Input is '+str(n)
        print 'Input is', 
        print n, 
        print 'days'
        
def cumulative(L):
    for i in range(2,len(L)):
        L[i]=L[i]+L[i-1]
    return L
        
def has_duplicates(L):
    for i in range(len(L)):
        for j in range(i):
            if L[i]==L[j]:
                return True
    return False
    
def probability(n, attempts):
    count=0
    for i in range(attempts):
        L=[]
        for i in range(n):
            day = randint(1,365)
            day = str(day)
            L.append(day)
        if has_duplicates(L):
            count = count + 1
    prob = float(count)/float(attempts)
    return prob
    
print probability(23, 10000)
    