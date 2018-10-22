#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 5 - CS166                                  #
# SMALL "ONE-TIME" PROGRAM TO RANDOMIZE LETTERS         #
# BARRY SMITH - OCT 23, 2018                            #
#########################################################



import random

def randomizeAlphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX0123456789"
    regAlphaList = list(alphabet)
    alphaList = list(alphabet)
    random.shuffle(alphaList)
    mixed = alphaList
  
    # Kind of weird to me. Does this just turn a list into string?
    print(*mixed, sep=',')
    print(mixed.index('h'))
    numVal = mixed.index('h')
    print(numVal)
    for x in mixed:
        #
        print(x)
        print(mixed.index(x))
        #print(alphaList.index(x))
        #print(mixed[x])
        print(regAlphaList[mixed.index(x)])
        print()
    # print(alphabet[numVal])      
    mixed = ''.join(mixed)
    print(mixed)
    
    
    
    
randomizeAlphabet()