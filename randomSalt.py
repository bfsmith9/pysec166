#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# SMALL PROGRAM TO RANDOMIZE LETTERS         #
# BARRY SMITH - NOV 6, 2018                            #
#########################################################



import random

plainWord = "cat"

def randomizeWord():
    alpha = "abcdefghijklmnopqrstuvwxyz"

    print("Here's the plainWord we're starting with: " + alpha)

    
    # Make a list out of word
    alpha = list(alpha)
    # Shuffle list mixed
    random.shuffle(alpha)  
    mixed = ''.join(alpha) 
    print(mixed)
    return mixed

randomizeWord()