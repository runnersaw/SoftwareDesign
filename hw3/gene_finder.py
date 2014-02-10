# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Sawyer Vaughan
"""

from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    protein = ''
    dna = dna.upper()
    numberCodons = len(dna) / 3 
    for i in range(len(dna)):
        if dna[i] != 'A' and dna[i] != 'T' and dna[i] != 'C' and dna[i] != 'G':
            print 'Must input valid amino acids'
            return
    for i in range(numberCodons):
        sequence = dna[(3*i):(3*i+3)]
        for j in range(21):
            currentCodons = codons[j]
            for k in range(len(currentCodons)):
                if sequence == currentCodons[k]:
                    index = j
        codon1 = aa[index]
        protein += codon1
    return protein
        
def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    tests = ['a', 'aa', 'ttt','tttttaattatggtttctcctactgcttattaacatcaaaataaagatgaatgttggcgtggt','ttttttttattattattgtg']
    expected = ['','','F','FLIMVSPTAY|HQNKDECWRG','FFLLLL']
    for i in range(len(tests)):
        result = coding_strand_to_AA(tests[i])
        print 'Input: ', tests[i], '\n','Expected output: ', expected[i], 'Actual output: ', result,'\n'

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    dna=dna.upper()
    for i in range(len(dna)):
        if dna[i] != 'A' and dna[i] != 'T' and dna[i] != 'C' and dna[i] != 'G':
            print 'Must input valid amino acids'
            return
    dna = dna[::-1]
    result = ''
    for i in range(len(dna)):
        if dna[i] == 'A':
            complement = 'T'
        elif dna[i] == 'T':
            complement = 'A'
        elif dna[i] == 'G':
            complement = 'C'
        elif dna[i] == 'C':
            complement = 'G'
        result += complement
    return result
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    tests = ['aaaaaa', 'gcgcgcgcgcgc', 'ttta','aaaacccc']
    expected = ['TTTTTT','GCGCGCGCGCGC','TAAA','GGGGTTTT']
    for i in range(len(tests)):
        result = get_reverse_complement(tests[i])
        print 'Input: ', tests[i], '\n','Expected output: ', expected[i], 'Actual output: ', result,'\n'

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    dna=dna.upper()
    numberCodons = len(dna) / 3
    extra = len(dna) % 3
    for i in range(len(dna)):
        if dna[i] != 'A' and dna[i] != 'T' and dna[i] != 'C' and dna[i] != 'G':
            print 'Must input valid amino acids'
            return
    result = ''
    for i in range(numberCodons):
        sequence = dna[(3*i):(3*i+3)]
        if sequence != 'TAA' and sequence != 'TAG' and sequence != 'TGA':
            result+=sequence
        else:
            return result
    result += dna[(len(dna)-extra):len(dna)]
    return result

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    tests = ['aa', 'cccccccccc', 'tga','tag','atgatgatgatgatgaaatag']
    expected = ['AA','CCCCCCCCCC','','','ATGATGATGATGATGAAA']
    for i in range(len(tests)):
        result = rest_of_ORF(tests[i])
        print 'Input: ', tests[i], '\n','Expected output: ', expected[i], 'Actual output: ', result,'\n'
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    dna=dna.upper()
    numberCodons = len(dna) / 3
    for i in range(len(dna)):
        if dna[i] != 'A' and dna[i] != 'T' and dna[i] != 'C' and dna[i] != 'G':
            print 'Must input valid amino acids'
            return
    i=0
    result = []
    while i < numberCodons:
        sequence = dna[(3*i):(3*i+3)]
        if sequence == 'ATG':
            result.append(rest_of_ORF(dna[3*i:]))
            i+=len(rest_of_ORF(dna[3*i:]))/3
        else:
            i+=1
    return result
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    tests = ['atg','atgtag','tatgtag','atgatgatgatgatgtagtagatggaa']
    expected = ['ATG','ATG','',['ATGATGATGATGATG','ATGGAA']]
    for i in range(len(tests)):
        result = find_all_ORFs_oneframe(tests[i])
        print 'Input: ', tests[i], '\n','Expected output: ', expected[i], 'Actual output: ', result,'\n'

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    dna=dna.upper()
    for i in range(len(dna)):
        if dna[i] != 'A' and dna[i] != 'T' and dna[i] != 'C' and dna[i] != 'G':
            print 'Must input valid amino acids'
            return
    result = []
    for i in range (3):
        if find_all_ORFs_oneframe(dna[i:])!=[]:
            result+=find_all_ORFs_oneframe(dna[i:])
    return result

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    tests = ['atgaatgatacatg','atgcatgcatgctagctagctagc','cccccatgcctag','aaaatagagtaaca']
    expected = [['ATGAATGAATG', 'ATGAATG', 'ATG'],['ATGCATGCATGC', 'ATGCATGCTAGC', 'ATGCTAGCTAGC'],['ATGCCTAG'],[]]
    for i in range(len(tests)):
        result = find_all_ORFs(tests[i])
        print 'Input: ', tests[i], '\n','Expected output: ', expected[i], 'Actual output: ', result,'\n'

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    result1=find_all_ORFs(dna)
    result2=find_all_ORFs(get_reverse_complement(dna))
    result = result1+result2
    return result

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    tests = ['ctaatgcattag','cat','ctacatcat','atgcat']
    expected = [['ATGCAT', 'ATGCAT'], ['ATG'], ['ATGATG'], ['ATGCAT', 'ATGCAT']]
    for i in range(len(tests)):
        result = find_all_ORFs_both_strands(tests[i])
        print 'Input: ', tests[i], '\n','Expected output: ', expected[i], 'Actual output: ', result,'\n'

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    temp = find_all_ORFs_both_strands(dna)
    maxLength = 0
    result=[]
    for i in range(len(temp)):
        length = len(temp[i])
        if length>maxLength:
            maxLength=length
            result = temp[i]
    return result       

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    tests = ['atgtagatgaaatagatgaaaaaatag','atgatgtagatggccc','atgtagcat','catatgtagctacat']
    expected = ['ATGAAAAAA','ATGGCCC','ATGCTACAT','ATG']
    for i in range(len(tests)):
        result = longest_ORF(tests[i])
        print 'Input: ', tests[i], '\n','Expected output: ', expected[i], 'Actual output: ', result,'\n'

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    from random import shuffle
    dna=dna.upper()
    for i in range(len(dna)):
        if dna[i] != 'A' and dna[i] != 'T' and dna[i] != 'C' and dna[i] != 'G':
            print 'Must input valid amino acids'
            return
    longest = 0
    for i in range(num_trials):
        dna = list(dna)
        shuffle(dna)
        dna = collapse(dna)
        lengthORF = len(longest_ORF(dna))
        if lengthORF>longest:
            longest = lengthORF
    return longest

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    ORFs = find_all_ORFs_both_strands(dna)
    temp=[]
    result=[]
    for i in range(len(ORFs)):
        if len(ORFs[i])>threshold:
            temp.append(ORFs[i])
    for i in range(len(temp)):
        result.append(coding_strand_to_AA(temp[i]))
    return result
