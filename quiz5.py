# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 16:08:30 2014

@author: sawyer
"""

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        
class Employee(Person):
    def __init__(self, name, date_of_birth, date_of_hire, salary):
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_hire = date_of_hire
        self.salary = salary
        
    def earns_more_than(self, salary):
        if self.salary > salary:
            return True
        return False
        
class Manager(Employee):
    def __init__(self, name, date_of_birth, date_of_hire, salary, direct_reports):
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_hire = date_of_hire
        self.salary = salary
        self.direct_reports = direct_reports
        
    def add_direct_report(self, new_report):
        self.direct_reports.append(new_report)

bob = Employee('Bob', 0726, 131, 9000)
jack = Employee('Jack', 0726, 131, 9000)
jon = Manager('Jon', 823, 923, 10000, [bob])

print jon.earns_more_than(100000)
jon.add_direct_report(jack)
print jon.direct_reports[1].name