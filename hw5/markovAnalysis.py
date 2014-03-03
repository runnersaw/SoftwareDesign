# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 12:45:40 2014

@author: griffin and sawyer, with much help and assistance from examples found
in Allen Downey's book Think Python
"""


import random
from pattern.web import *

def tweets_to_text(twitterhandle):
    t = Twitter(language='en') 
    textfile = open('tweets.txt', 'w')
    i = None
    if t.search('from:'+twitterhandle, start=i, count=1)==[]:
        raise SystemExit("Sorry, your celebrity doesn't have any recent tweets")
    for j in range(3):
        for tweet in t.search('from:'+twitterhandle, start=i, count=100):
            textfile.write(' '+tweet.text)
            i = tweet.id
    textfile.close()
    return textfile
    

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order):
    """This function will open a txt file and perform Markov analysis

    filename: string
    order: integer number of words in the prefix

    Returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename)
    

    for line in fp:
        #This gets rid of excess whitespace and splits the file into the 
        #individual words.
        for word in line.rstrip().split():
            if word[0] != '@' and word[0:4] != 'http':
                process_word(word, order)
    




def process_word(word, order):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words; 
    after that we start adding entries to the dictionary.
    """
    # this adds words to the prefixes until it's the length of the order
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        #this will add another word to the tuple value for the prefix key
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]
    

    prefix = shift(prefix, word)


def random_text(n):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(suffix_map.keys())
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print word,
        start = shift(start, word)


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    
    We need to use a tuple for creating the new prefix instead of a string
    """
    
    #adds the new word to start of the tuple
    return t[1:] + (word,)


def main_markov(filename, n, order):
    print 'Here is your new tweet: \n'
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else: 
        process_file(filename, order)
        random_text(n)


if __name__ == '__main__':
    tweets_to_text('kellyoxford')
    main_markov('tweets.txt', 30,1)