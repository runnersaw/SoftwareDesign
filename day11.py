# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:25:17 2014

@author: sawyer
"""

def exclusive_or_dict(d1,d2):
    d = {}
    for key in d1:
        if key in d2:
            pass
        else:
            d[key]=d1[key]
    for key in d2:
        if key in d1:
            pass
        else:
            d[key]=d2[key]
    return d

