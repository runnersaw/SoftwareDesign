# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 15:19:48 2014

@author: sawyer
"""

def sum_squares_even(n):
    tot = 0
    for i in range(n+1):
        if i%2 == 0:
            tot += i**2
    return tot
    
def pair_list_to_dictionary(l):
    d = {}
    length = len(l)
    if length%2 != 0:
        length = length-1
    for i in range(length/2):
        d[l[2*i]] = l[2*i+1]
    return d
    
def split_dictionary(d):
    d1 = {}
    d2 = {}
    for key in d:
        if key[0].isupper():
            d1[key] = d[key]
        elif key[0].islower():
            d2[key] = d[key]
    return[d1, d2]
    
def in_language(string):
    if len(string)%2 != 0:
        return False
    s1 = string[:len(string)/2]
    s2 = string[len(string)/2:]
    for i in range(len(s1)):
        if s1[i] != 'a':
            return False
    for i in range(len(s2)):
        if s2[i] != 'b':
            return False
    return True
    
class DNASequence:
    ''' Represents a sequence of DNA '''
    def __init__(self, nucleotides):
        ''' Constructs a DNASequence with the specified nucleotides. 
        nucleotides: the nucleotides represented as a string of capital letters in ['A','C','G','T'] '''
        self.nucleotides = nucleotides
        
    def get_reverse_complement(self):
        string = ''
        d = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        for i in range(len(self.nucleotides)):
            string += d[self.nucleotides[i]]
        complement = DNASequence(string)
        return complement
        
    def get_proportion_ACGT(self):
        d = {'A':0, 'T':0, 'C':0, 'G':0}
        tot = float(len(self.nucleotides))
        for i in range(len(self.nucleotides)):
            d[self.nucleotides[i]] += 1
        for key in d:
            d[key] = d[key]/tot
        return d
    
    
if __name__ == "__main__":
    print sum_squares_even(11)
    print pair_list_to_dictionary(['hello','a','test','b',4])
    print split_dictionary({'a':2, 'B':'hello', 'c':'t'})
    print in_language('abbb')
    sequence = DNASequence('AGCGGGTT')
    x = sequence.get_reverse_complement()
    print x.nucleotides
    print sequence.get_proportion_ACGT()