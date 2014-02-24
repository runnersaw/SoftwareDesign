# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:27:09 2014

@author: sawyer
"""

from swampy.TurtleWorld import *

def snow_flake_side(t,sidelength,level):
    '''draws one side of the Kock snowflake with sidelength and recursion level defined. '''
    t.delay=.001/(4.0**level)
    if level == 1:
        sidelength=float(sidelength)
        fd(t,sidelength/3)
        rt(t,60)
        fd(t,sidelength/3)
        lt(t,120)
        fd(t,sidelength/3)
        rt(t,60)
        fd(t,sidelength/3)
    else:
        snow_flake_side(t,sidelength/3.0,level-1)
        rt(t,60)
        snow_flake_side(t,sidelength/3.0,level-1)
        lt(t,120)
        snow_flake_side(t,sidelength/3.0,level-1)
        rt(t,60)
        snow_flake_side(t,sidelength/3.0,level-1)
        
def snow_flake(t,sidelength,level):
    '''draws the whole Koch snowflake with sidelength and recursion level defined'''
    snow_flake_side(t,sidelength,level)
    lt(t,120)
    snow_flake_side(t,sidelength,level)
    lt(t,120)
    snow_flake_side(t,sidelength,level)
    lt(t,120)
    
def recursive_tree(t,sidelength,level):
    '''draws a fractal tree with sidelength and level'''
    t.delay == 0
    if level == 1:
        fd(t,sidelength)
        set_pen_color(t,'brown')
    else:
        set_pen_color(t,'brown')
        fd(t,sidelength)
        clone = Turtle()
        clone.x = t.x
        clone.y = t.y
        clone.heading = t.heading
        clone.delay = 0
        lt(clone, 30)
        set_pen_color(clone,'green')
        recursive_tree(clone,sidelength*.5,level-1)
        die(clone)
        bk(t,sidelength/3.0)
        clone = Turtle()
        clone.x = t.x
        clone.y = t.y
        clone.heading = t.heading
        clone.delay = 0
        rt(clone,40)
        set_pen_color(clone,'green')
        recursive_tree(clone,sidelength*.6,level-1)
        die(clone)
        bk(t,sidelength/6.0)
        clone = Turtle()
        clone.x = t.x
        clone.y = t.y
        clone.heading = t.heading
        clone.delay = 0
        lt(clone,45)
        set_pen_color(clone,'green')
        recursive_tree(clone,sidelength*.4,level-1)
        die(clone)
        bk(t,sidelength/6.0)
        clone = Turtle()
        clone.x = t.x
        clone.y = t.y
        clone.heading = t.heading
        clone.delay = 0
        rt(clone,50)
        set_pen_color(clone,'green')
        recursive_tree(clone,sidelength*.2,level-1)
        die(clone)

def save_turtle_state(turtle_states,t):
    turtle_states.append((t.x,t.y,t.heading))

def restore_turtle_state(turtle_states,t):
    s = turtle_states.pop()
    t.x = s[0]
    t.y = s[1]
    t.heading = s[2]
    
if __name__ == '__main__':
    world = TurtleWorld()
    griffin = Turtle()
    griffinsucks = Turtle()
    griffin.y = -200
    recursive_tree(griffin,400,7)
    snow_flake(griffinsucks, 300,5)
    wait_for_user()