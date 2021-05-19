#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:22:19 2021

@author: Thomas Davies
"""

from nltk.tokenize import word_tokenize
import numpy as np
import pandas as pd



#Get and store all text

file = open("moreMarvel.txt",encoding="utf-8")
lines = file.read().replace("\n", "").split(".")
file.close()


#Put all words in a list

bag = []
for line in lines:
    if ( line != "" ):
        tokens = word_tokenize(line)
        for i,token in enumerate(tokens):
            if ( token.isalnum() ):
                bag.append( token.lower() )


#Count the number of times each word appears and store as a k/v pair

d = { "temp" : {"temp" : 0 } }

first = bag[0]
for second in bag[1:]:
    if first in d:
        if second in d[first]:
            d[first][second] = d[first][second] + 1
        else:
            d[first][second] = 1
    else:
        d[first] = { second : 1 }

    first = second

#Do an extra one for the last word of the corpus
if first in d:
    d[first][''] = 1
else:
    d[first] = { '' : 1 }


#Find the total number of words
total = 0
for words in d.values():
    for num in words.values(): 
        total += num    

probabilities = { "temp" : 0 }

#Calculate the probability of each word appearing
for word in bag:
    probabilities[word] = 0
    for w in d[word]:
        probabilities[word] += d[word][w] / total


#Create lists of keys and probs
keys = []
for key in d.keys():
    keys.append(key)

probs = []
for prob in probabilities.values():
    probs.append(prob)


#Choose a random starting word
previous = np.random.choice( keys, p = probs, size = 1 )[0]
print( previous + " ", end = '' )

#Choose 15 random words based on bigram model
for i in range( 15 ):
    validBigrams = []
    tempTotal = 0

    for word in d[previous].keys():
        validBigrams.append(word)
        tempTotal += d[previous][word]

    chances = []
    for chance in d[previous].keys():
        chances.append( d[previous][chance] / tempTotal )

    previous = np.random.choice( validBigrams, p = chances, size = 1 )[0]  
    print ( previous + " ", end = '' )

print()


