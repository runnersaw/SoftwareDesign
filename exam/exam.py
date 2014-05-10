# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 15:21:17 2014

@author: sawyer
"""

def sum_numbers_not_divisible_by_four(n):
    total = 0
    for i in range(n+1):
        if i%4 != 0:
            total+=i
    return total
    
def count_frequencies_of_first_letters(L):
    res = {}
    for word in L:
        firstLetter = word[0]
        if firstLetter in res:
            res[firstLetter]+=1
        else:
            res[firstLetter]=1
    return res
    
def compute_binomial_coeff_recursive(n,k):
    if n==k:
        return 1
    if k==0:
        return 1
    return compute_binomial_coeff_recursive(n-1,k-1)+compute_binomial_coeff_recursive(n-1,k)
    
class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        
    def is_before(self, other_date):
        if self.year < other_date.year:
            return True
        elif self.year == other_date.year:
            if self.month < other_date.month:
                return True
            elif self.month == other_date.month:
                if self.day < other_date.day:
                    return True
        return False
        
    def increment_year(self):
        self.year += 1
        
class PointND(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        
    def distance(self, other):
        totSquare = 0
        for i in range(len(self.coordinates)):
            totSquare += (self.coordinates[i]-other.coordinates[i])**2
        return totSquare**(.5)
        
class Point3D(PointND):
    def __init__(self, x, y, z):
        PointND.__init__(self, [x,y,z])
                
    
if __name__=="__main__":
    print sum_numbers_not_divisible_by_four(5)
    print count_frequencies_of_first_letters(['hello','goodbye','hi','huh'])
    print compute_binomial_coeff_recursive(6,5)
    d1 = Date(5,20,1995)
    d2 = Date(5,31,1995)
    print d1.is_before(d2)
    d1.increment_year()
    print d1.year
    print d1.is_before(d2)
    p1 = PointND([0,4])
    p2 = PointND([3,0])
    p3 = PointND([1,1,1])
    p4 = Point3D(1,4,5)
    print p1.distance(p2)
    print p4.distance(p3)
    print range(4)