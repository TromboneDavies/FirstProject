from nltk.tokenize import word_tokenize
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator

def get_words(text):
    file = open(text)
    lines = file.read().replace("\n", "").split(".")
    file.close()

    words = []
    for line in lines:
        if ( line != "" ):
            tokens = word_tokenize( line )
            for token in tokens:
                if ( token.isalnum() ):
                    words.append( token.lower() )

    return words

def lexical_diversity(text):
    words = get_words(text)
    print(text + ":\n\ttypes: " + str(len(set(words))) + "\n\ttokens: " +
    str(len(words)))
    return ( len( set( words ) ) / len(words) )

def word_lengths(text):
    words = get_words(text)

    lengths = [ len(word) for word in words ]

    plt.clf()
    plt.hist(lengths, bins=range(1,40), density = True)
    plt.title(text)
    plt.savefig(text + ".png")

def sentence_lengths(text):
    file = open(text)
    sentences = file.read().replace("\n", "").split(".")
    file.close()
    sentence_lengths = [ len(setence.split(" ")) for setence in sentences ]

    plt.clf()
    plt.hist(sentence_lengths, bins=range(1,40), density = True)
    plt.title(text)
    plt.savefig(text + "Sentence.png")

def top_bigrams(text):
    words = get_words(text)
    bigrams = list(nltk.bigrams(words))
    freq = { "" : 0 }
    for bigram in bigrams:
        if bigram in freq:
            freq[bigram] = freq[bigram] + 1
        else:   
            freq[bigram] = 1

    topBiFreq = sorted(freq.items(), key = operator.itemgetter(1))
    print("Top 10 bigrams for " + text + ":")
    for i in range(1, 11):
        print("\t" + str(topBiFreq[-i]))
    print()

lexicalDiversity = input("Would you like the lexical diversity of each corpus? (y/n)\n")
if ( lexicalDiversity == "y" ):
    print("\tLexical Diversity: " + str(lexical_diversity("moreMarvel.txt")))
    print("\tLexical Diversity: " + str(lexical_diversity("billyjoel.txt")))
    print("\tLexical Diversity: " + str(lexical_diversity("Sherlock.txt")))
    print("\tLexical Diversity: " + str(lexical_diversity("HP1+2.txt")))

wordLengths = input("Would you like the word lengths of each corpus?  (y/n)\n")
if ( wordLengths == "y" ):
    word_lengths("moreMarvel.txt")
    word_lengths("billyjoel.txt")
    word_lengths("Sherlock.txt")
    word_lengths("HP1+2.txt")

sentenceLengths = input("Would you like the sentence lengths of each corpus? (y/n)\n")
if ( sentenceLengths == "y" ):
    sentence_lengths("moreMarvel.txt")
    sentence_lengths("billyjoel.txt")
    sentence_lengths("Sherlock.txt")
    sentence_lengths("HP1+2.txt")
    
topBigrams = input("Would you like the top 10 bigrams of each corpus? (y/n)\n")
if ( topBigrams == "y" ):
    top_bigrams("moreMarvel.txt")
    top_bigrams("billyjoel.txt")
    top_bigrams("Sherlock.txt")
    top_bigrams("HP1+2.txt")

