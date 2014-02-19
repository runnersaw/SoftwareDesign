# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: svaughan
"""
from math import *
from random import randint
import Image

def build_random_function(min_depth, max_depth):
    ''' This function builds a random function, with a specified minimum depth of nested functions
    and a specified maximum depth of nested functions
    
    I added division to make the function more interesting. The function always divides
    the smaller number by the bigger so it produces a number less than 1
    
    Every once in a while, I seem to be getting an error evaluating division, just try again.
    '''

    #This section picks a function
    function=[]
    functions=['prod','div','sin_pi','cos_pi']
    functionNum=randint(0,len(functions)-1) #picks a function
    function.append(functions[functionNum])
    
    #next section is the end conditions    
    if min_depth <= 1:
        if max_depth == 1: #means that it's reached max depth
            if functionNum <= 1:
                function.extend(['X','Y'])
            else:
                addXY=randint(0,1) #will add x, y or both depending on value
                if addXY==0:
                    function.append('X') #Using capitals for the variables and not the functions
                elif addXY==1:
                    function.append('Y')
            return function
        else:
            odds = randint(0,max_depth)
            if odds == 0: #done this way, there should be equal chance of ending at each value between min and max depth
                if functionNum <= 1:
                    function.extend(['X','Y'])
                else:
                    addXY=randint(0,1) #will add x, y or both depending on value
                    if addXY==0:
                        function.append('X') #Using capitals for the variables and not the functions
                    elif addXY==1:
                        function.append('Y')
                return function
        
    if functionNum<=1:
        addX=randint(0,2) #will add x, y or both depending on value
        if addX==1:
            function.append('X') #Using capitals for the variables and not the functions
        elif addX==2:
            function.append('Y')
        else:
            add2 = build_random_function(min_depth-1,max_depth-1)
            function.append(add2)
    
    #next section picks a function
    add = build_random_function(min_depth-1,max_depth-1)
    function.append(add)
    return function
    
def division(x,y):
    '''returns x/y if y>x and y/x if x/y. Thus the value returned can never be 
    greater than 1 '''
    if x>=y:
        return y/x
    else:
        return x/y
    
if __name__ == '__main__':
    x = build_random_function(5,5)
    print x
    
def evaluate_random_function(f, x, y):
    ''' This function takes a function in the form provided by build_random_function and evaluates
    it at the value x, y 
    
    Every once in a while, I seem to be getting an error evaluating division, just try again.
    '''

    for i in range(len(f)-1):
        if f[i] == 'sin_pi': 
            if f[i+1] == 'X': 
                return sin(pi*x)
            if f[i+1] == 'Y':
                return sin(pi*y)
            else:
                return sin(pi*evaluate_random_function(f[i+1],x,y))
        if f[i] == 'cos_pi':
            if f[i+1] == 'X': 
                return cos(pi*x)
            if f[i+1] == 'Y':
                return cos(pi*y)
            else:
                return sin(pi*evaluate_random_function(f[i+1],x,y))
        if f[i] == 'prod':
            if f[i+1] == 'X' and f[i+2] == 'Y': 
                return x*y
            elif f[i+1] == 'Y':
                return y*evaluate_random_function(f[i+2],x,y)
            elif f[i+1] == 'X':
                return x*evaluate_random_function(f[i+2],x,y)
            else:
                return evaluate_random_function(f[i+1],x,y)*evaluate_random_function(f[i+2],x,y)
        if f[i] == 'div':
            if f[i+1] == 'X' and f[i+2] == 'Y': 
                return division(x,y)
            elif f[i+1] == 'Y':
                return division(y, evaluate_random_function(f[i+2],x,y))
            elif f[i+1] == 'X':
                return division(x,evaluate_random_function(f[i+2],x,y))
            else:
                return division(evaluate_random_function(f[i+1],x,y),evaluate_random_function(f[i+2],x,y))

if __name__ == '__main__':
    print evaluate_random_function(x,.25,.75)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    
    val=float(val)
    input_interval_start=float(input_interval_start)
    input_interval_end=float(input_interval_end)
    output_interval_start=float(output_interval_start)
    output_interval_end=float(output_interval_end)
    
    coefficient = (val-input_interval_end)/(input_interval_start-input_interval_end)
    value = output_interval_end-coefficient*(output_interval_end-output_interval_start)
      
    return value    

def generate_image(imagename,min_depth,max_depth):
    ''' Generates an image of the random functions with specified min and max depths
    for blue red and green pixel colors and saves it as an image with the name imagename
    '''
    
    red_func = build_random_function(min_depth,max_depth)
    blue_func = build_random_function(min_depth,max_depth)
    green_func = build_random_function(min_depth,max_depth)
    
    im = Image.new("RGB",(350,350),0)
    
    pixels=im.load()
    
    for i in range(350):
        for j in range(350):
            x = remap_interval(i,0,349,-1,1)
            y = remap_interval(j,0,349,-1,1)
            red_value = int(remap_interval(evaluate_random_function(red_func, x, y),-1,1,0,255))
            green_value = int(remap_interval(evaluate_random_function(green_func, x, y),-1,1,0,255))
            blue_value = int(remap_interval(evaluate_random_function(blue_func, x, y),-1,1,0,255))
            if red_value <0:
                red_value = 0
            if red_value > 255:
                red_value = 255
            if green_value <0:
                green_value = 0
            if green_value > 255:
                green_value = 255
            if blue_value <0:
                blue_value = 0
            if blue_value > 255:
                blue_value = 255
            
            pixels[i,j]=red_value,green_value,blue_value
            
    im.save(imagename,'png')

