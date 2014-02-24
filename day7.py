# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:27:23 2014

@author: sawyer
"""

def sum_of_squares(n):
    s = 0
    for i in range(n):
        s+=(i+1)**2
    return s
    
def filter_out_negative_numbers(l):
    newList=[]
    for i in range(len(l)):
        if l[i]>=0:
            newList.append(l[i])
    return newList

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
    
