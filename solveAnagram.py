#!/usr/bin/python

import sys
import difflib
import argparse

parser = argparse.ArgumentParser(description='Dude stop messing around and pay attention to the arguments.')
parser.add_argument('-d','--dictionary', default='dictionary.csv', type=argparse.FileType('r'), help='File to lookup potential matches for the input strings')
parser.add_argument('-s', '--strings',  nargs='+',help='List of strings to lookup')
args = vars(parser.parse_args())

dictionary = args['dictionary']
anagrams = args['strings']

lines = dictionary.readlines()

sortedDict = {}
for name in lines:
    sortedName = ''.join(sorted(list(str.lower(name[:-1]).replace(" ", ""))))
    sortedDict[sortedName] = str(name)

for anagram in anagrams:

    result = {}
    print "Trying " + anagram

    inputString = ''.join(sorted(list(str.lower(anagram.replace(" ", "")))))

    for key in sortedDict:
        diff_ratio = difflib.SequenceMatcher(None, key, inputString).ratio()
        if diff_ratio > 0.8:
            result[diff_ratio] = sortedDict[key]
    
    if len(result) > 0:
        print "Found possible solutions:"
        for key, value in result.iteritems():
            print value.rstrip() + " (" + str(key * 100) + "%" +")"
    else: 
        print "No match found"

    dictionary.close()

