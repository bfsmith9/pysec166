#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# PROGRAM TO CRACK PASSWORDS                            #  
# BARRY SMITH - OCT 30, 2018                            #
#########################################################

# import time
import hashlib, sys, io

hash_file = "hashes_source.txt"
wordlist = "wordlist800.txt"
passwordHash = []
data = []

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
# timer = time()

for line in hashSource:
    # line = line.replace("\n", "")
    # print(line)
    passwordHash.append(line) 
    

# iterate through hash/pw combos, testing wordlist file 
# ...etc. - see JR's code
# He hashes each word he writes in and compares to original hash source
# About 70 lines of code.


# with io.open(wordlist, encoding='utf-8') as wordsFile:
with io.open(wordlist, encoding='utf-8') as wordsFile:
    for i in wordsFile.readlines():
        i = i.replace("\n","")
        data.append(i)


print(data[0])
print(data[1])
print(data[2])
print(passwordHash[0])

for element in data:
    print(element)
    hashResult=hashlib.md5(element.encode()).hexdigest()
    #hashResult = element.hexdigest()
    if (hashResult == passwordHash[0]):
        print("Hello, what have we here?")
        print("The word " + element + " has the md5digest " + hashResult)
        print("This matches ")
    else:
        print("No dice - " + hashResult)
        

