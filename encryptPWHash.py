#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# ADD HASH ENCRYPTION TO INTRANET PROGRAM                    #
# BARRY SMITH - NOVEMBER 6, 2018                        #
#########################################################


import csv
import re

from randomSalt import randomizeWord
from hashFunction import hashPassword

#from randomizeAlpha import encryptedWord

true = 1
false = 0


# FUNCTIONS AREA
# ----------------------------------------
# login function. When program starts, this is the first function,
# where a user needs to login. A file in local storage contains a list
# of names, passwords, and access-levels. This is read in before user
# interaction begins.
        
def login(userList):
    # At first, userList is a blank dictionary
    pwSalt = randomizeWord()
    loadUsers(userList, filename)
    # How to input with spaces after name?
    try:
        userNameInput = input("Please input your username: ")
        name = userNameInput.strip()
        # HANDLING SIMULATED BUFFER OVERFLOW
        while (len(name) > 25):
            print("Username must be less than 25 characters - please try again.")
            userNameInput = input("Please input your username: ")
            name = userNameInput.strip()
        
        if (not(name in userList)):
            newUserPasswordInput = input("Please enter a new password \n")
            print(newUserPasswordInput)
            # PASSWORD REVIEW
            while( (len(newUserPasswordInput) < 8) or ( (len(newUserPasswordInput) > 25) ) ):
                print("Password has to be between 8 & 25 characters - please try again.")
                newUserPasswordInput = input("Please enter a new password \n")

            userList[name] = {}
            # userList[name]["Password"] = newUserPasswordInput.strip()
            pw = newUserPasswordInput.strip()
            # epw = encryptWord(pw)
            hashedPW = hashPassword(pw, pwSalt)
            userList[name]["Password"] = hashedPW
            userList[name]["Access_Level"] = "3"
            userList[name]["Salt"] = pwSalt

            
            line = name + ",Password," + hashedPW + ",Access_Level,1," + "Salt," + pwSalt
            print(line)
            with open(filename, 'a') as data_file:
            
                data_file.write(line)
                data_file.write('\n')
               
            
        userPasswordInput = input("Please input your password: ")
        pw = userPasswordInput.strip()
               
        checkWord = userList[name]["Password"]
        chkSalt = userList[name]["Salt"]
        dCheckWord = hashPassword(pw, chkSalt)
        if (dCheckWord == checkWord):
        #if (userList[name]["Password"] == pw):
            print("You are logged in, " + name)
            return name
            
        else:
            print("Incorrect password. Exiting program.")
            exit()
    except KeyError:
        print("That was not a valid username. Please try again. Exiting program")
        exit()

# enterReportingArea function. Allows users to enter the lowest-level
# "Reporting" area of app


def enterReportingArea(name, users):
    if ((users[name]["Access_Level"] == "1") or (users[name]["Access_Level"] == "2") or (users[name]["Access_Level"] == "3")):
        print ("You have now entered the Reporting application.")
    else:
        print("You do not have permission to use this application.")

# enterDevelopmentArea function. Allows users to enter the mid-level
# "Development" area of app
        
def enterDevelopmentArea(name, users):
    if ((users[name]["Access_Level"] == "1") or (users[name]["Access_Level"] == "2")):
        print ("You have now entered the Development application.")
    else:
        print("You do not have permission to use this application.")
 
# enterFinanceArea function. Allows users to enter the high-level
# "Finance" area of app
   
def enterFinanceArea(name, users):
    if (users[name]["Access_Level"] == "1"):
        print ("You have now entered the Finance application.")
    else:
        print("You do not have permission to use this application.")

# loadUsers function. This is executed immediately upon program startup.
# It loads existing users names, passwords, and access levels from a 
# csv file stored locally. If a user is not in this file, the program
# will terminate.

def loadUsers(areas,filename):
    try:
        with open(filename, 'r') as data_file:
            data = csv.DictReader(data_file, delimiter=",")
            for row in data:
                item = areas.get(row["Name"], dict())
                item[row["Password"]] = row["pass"]
                item[row["Access_Level"]] = row["number"]
                item[row["Salt"]] = row["saltString"]

                areas[row["Name"]] = item
                print(areas.keys())
                print(areas.values())
    
    except FileNotFoundError:
        print("File not found! Please check your directory for the {} file.".format(filename))
        print("Program terminating.")
        exit()

# printMenu function. Central navigation menu for users
def printMenu():
    print('1. Menu')
    print('2. Enter Reporting Application')
    print('3. Enter Development Application')
    print('4. Enter Finance Application')
    print('8. Quit')

    print()


def encryptWord(plainWord, randomizedAlpha):  
    print("Here's the plainWord we're starting with: " + plainWord)
    plainNumCode = []
    encryptedWord = []
    
    # Actual alphabet - upper- and lowercase, numbers
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX0123456789"

    print(alphabet)
    print(randomizedAlpha)
    
    # Make a list out of the plainWord
    wordCharList = list(plainWord)
    alphaList = list(alphabet)

    
    # Put the plainWord into its numeric form - from the position in regular alphabet order
    for y in wordCharList:
        plainNumCode.append(alphaList.index(y))
    print(plainNumCode)
    for z in plainNumCode:
        encryptedWord.append(randomizedAlpha[z])
    print(encryptedWord)
    encryptedWord = ''.join(encryptedWord)
    print(encryptedWord)
    return encryptedWord

def decryptWord(encryptedWord, randomizedAlpha):
    print("Here's the encrypted word we're starting with: " + encryptedWord)
    decryptedWord = []
    encryptedNumCode = []

    # Actual alphabet - upper- and lowercase, numbers
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX0123456789"

    print(alphabet)
    print(randomizedAlpha) 
    
    # Make a list out of the encrypted word
    encryptedCharList = list(encryptedWord)
    # Put the encrypted word into its numeric form - from the position in regular alphabet order
    randomizedAlphaList = list(randomizedAlpha)
    
    for y in encryptedCharList:
        encryptedNumCode.append(randomizedAlphaList.index(y))
    print(encryptedNumCode)
    for z in encryptedNumCode:
        decryptedWord.append(alphabet[z])
    print(decryptedWord)
    decryptedWord = ''.join(decryptedWord)
    print(decryptedWord)
    return decryptedWord

def hashEncrypt(plainWord, salt):
    print("Here's a plain old word: " + plainWord)
    
def hashDecypt(hashedWord, salt):
    print("Here's a hashed word " + hashedWord)         

# MAIN EXECUTION AREA -----------------------------------

# Create a userList dictionary - empty at first
userList = {}
filename = "usersWithSalts.txt"
plainWord = "cat"
alpha = "abcdefghijklmnopqrstuvwxyz"


print("Welcome!")
name = login(userList)
menu_choice = 0
printMenu()
while menu_choice != "8":
    try:
        menu_choice = input("Type in a number (1-8, 0 for menu): ")
        if menu_choice == "1":
            printMenu()
        elif menu_choice == "0":
            printMenu()
        elif menu_choice == "2":
            enterReportingArea(name, userList) 
        elif menu_choice == "3":
            enterDevelopmentArea(name, userList)     
        elif menu_choice == "4":
            enterFinanceArea(name, userList)           
        elif menu_choice == "8":
            #exit
            pass
        else:
            printMenu()
    except SyntaxError:
        print("That was not a number.")

# encryptedWord = encryptWord(plainWord, randomizedAlpha)
# decryptWord(encryptedWord, randomizedAlpha)

print("Goodbye")
# randomizeWord(alpha)
