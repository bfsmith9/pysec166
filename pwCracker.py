#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# PROGRAM TO CRACK PASSWORDS                            #  
# BARRY SMITH - OCT 30, 2018                            #
#########################################################


import hashlib, sys, time

hash_file = "hashes_source.txt"
wordlist = "wordlist800.txt"

# read hash from hash file

try:
   hashSource = open(hash_file, "r")

except IOError:
    print("Problem with hash file on disk")
    sys.exit()

# read wordlist
try:
    wordListFile = open(wordlist, "r")

except IOError:
    print("Problem with wordlist file on disk.")
    sys.exit()

# initialize vars
test = 0
cracked = 0
timer = time()

# iterate through hash/pw combos, testing wordlist file 
# ...etc. - see JR's code
# He hashes each word he writes in and compares to original hash source
# About 70 lines of code.
