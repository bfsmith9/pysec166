#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# PROGRAM TO CRACK PASSWORDS                            #  
# BARRY SMITH - OCT 30, 2018                            #
#########################################################

import hashlib, sys, io

hash_file = "hashes_source.txt"
wordlist = "wordlist800.txt"
passwordHash = []
data = []
numberAttempts = 0

# read hash from hash file
try:
    hashSource = open(hash_file, "r")

except IOError:
    print("Problem with hash file on disk.")
    sys.exit()

# read word list
try:
    wordListFile = open(wordlist, "r")

except IOError:
    print("Problem with word list file on disk.")
    sys.exit()

# initialize vars
test = 0
cracked = 0

for line in hashSource:
    passwordHash.append(line) 
    

# iterate through hash/pw combos, testing wordlist file 
with io.open(wordlist, encoding='utf-8') as wordsFile:
    for i in wordsFile.readlines():
        i = i.replace("\n","")
        data.append(i)

for element in data:
    print(element)
    hashResult=hashlib.md5(element.encode()).hexdigest()

    if (hashResult == passwordHash[0]):
        print("Hello, what have we here?")
        print("The word " + element + " has the md5digest " + hashResult)
        print("This matches " + passwordHash[0])
        numberAttempts = numberAttempts + 1
        print("numberAttempts: ", numberAttempts)
        print("Program now terminating.")
        break
    else:
        print("No dice - " + hashResult)
        numberAttempts = numberAttempts + 1
        print("numberAttempts: ",  numberAttempts)
        print("---")
        


