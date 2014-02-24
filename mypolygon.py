# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:48:30 2014

@author: sawyer
"""
from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print bob

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)
        
def polygon(t, n):
    for i in range(n):
        fd(t,100)
        lt(t,360/n)
        
def circle(t, r, angle):
    sides=100
    for i in range(sides*angle/360):
        fd(t,2.0*math.pi*r/sides)
        lt(t,360.0/sides)
        
bob.delay=.01
    
circle(bob, 100, 180)
bob.delay=.1
square(bob)
polygon(bob,7)

wait_for_user()
