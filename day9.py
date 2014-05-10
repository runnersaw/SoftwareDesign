# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:27:27 2014

@author: sawyer
"""

def recursive_flatten(l):
    res = []
    for element in l:
        if type(element)==list:
            res.extend(recursive_flatten(element))
        else:
            res.append(element)
    return res
    
print recursive_flatten([1,2,[3,5]])
print recursive_flatten([1,2,[3,['asdf',4.0]],3])
print recursive_flatten([1,5,[1,3],5.0,['test','testing'],'blah'])