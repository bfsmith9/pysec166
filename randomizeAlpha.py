#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 5 - CS166                                  #
# SMALL "ONE-TIME" PROGRAM TO RANDOMIZE LETTERS         #
# BARRY SMITH - OCT 23, 2018                            #
#########################################################



import random

def randomizeAlphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX0123456789"
    # Make a list out of alphabet
    alphaList = list(alphabet)
    # Make another list out of alphabet called mixed
    mixed = list(alphabet)
    # Shuffle list mixed
    random.shuffle(mixed)  
    
    # Kind of weird to me. Does this just turn a list into string?
    print(*mixed, sep=',')
    print(mixed.index('h'))
    numVal = mixed.index('h')
    print(numVal)
    for x in mixed:
        #
        # Print value in mixed
        print(x)
        # Print that mixed value's index
        print(mixed.index(x))
        #print(alphaList.index(x))
        #print(mixed[x])
        # Print what's in the alphaList at the same index
        print(alphaList[mixed.index(x)])
        print()
    # print(alphabet[numVal])      
    mixed = ''.join(mixed)
    print(mixed)
    
    
    
    
randomizeAlphabet()