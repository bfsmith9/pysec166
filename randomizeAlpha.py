#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 5 - CS166                                  #
# SMALL "ONE-TIME" PROGRAM TO RANDOMIZE LETTERS         #
# BARRY SMITH - OCT 23, 2018                            #
#########################################################



import random

plainWord = "cat"
plainNumCode = []
encryptedWord = []
encryptedNumCode = []

def randomizeAlphabet(plainWord):
    
    print("Here's the plainWord we're starting with: " + plainWord)
    
    plainNumCode = []
    encryptedWord = []
    decryptedWord = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX0123456789"
    print(alphabet)
    # Make a list out of alphabet
    alphaList = list(alphabet)
    # Make another list out of alphabet called mixed
    mixed = list(alphabet)
    # Shuffle list mixed
    random.shuffle(mixed)  
    
    # Kind of weird to me. Does this just turn a list into string?
    # print(*mixed, sep=',')
    # print(mixed.index('h'))
    # numVal = mixed.index('h')
    # print(numVal)
    # for x in mixed:
        #
        # Print value in mixed
        # print(x)
        # Print that mixed value's index
        # print(mixed.index(x))

        # Print what's in the alphaList at the same index
        # print(alphaList[mixed.index(x)])
        # print()
    # print(alphabet[numVal])      
    mixed = ''.join(mixed)
    print(mixed)
    
    # Make a list out of the plainWord
    wordCharList = list(plainWord)
    
    # Put the plainWord into its numeric form - from the position in regular alphabet order
    for y in wordCharList:
        plainNumCode.append(alphaList.index(y))
    print(plainNumCode)
    for z in plainNumCode:
        encryptedWord.append(mixed[z])
    print(encryptedWord)
    encryptedWord = ''.join(encryptedWord)
    print(encryptedWord)
    
    # Make a list out of the encrypted word
    encryptedCharList = list(encryptedWord)
    
    # Put the encrypted word into its numeric form - from the position in regular alphabet order
    mixedList = list(mixed)
    for y in encryptedCharList:
        encryptedNumCode.append(mixedList.index(y))
    print(encryptedNumCode)
    for z in encryptedNumCode:
        decryptedWord.append(alphabet[z])
    print(decryptedWord)
    decryptedWord = ''.join(decryptedWord)
    print(decryptedWord)    
    
randomizeAlphabet(plainWord)