#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 1 - CS166                                  #
# PROGRAM TO MANAGE PASSWORDS & ACCESS LEVELS FOR USERS #
# BARRY SMITH - SEPT 11, 2018                           #
#########################################################


import csv
import random
from randomizeAlpha import encryptedWord

true = 1
false = 0

# Actual alphabet - upper- and lowercase
# alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX0123456789"

# Here is a randomized alphabet. Each character in this alphabet
# will be associated with a character in the actual alphabet.
# That will be the encryption used.
randomizedAlpha = "osWBnrX8GwlAb1O4dvN2RcEgik9j7L0JztqhUmPyFpK35DxQMVCT6aSHIfeu"

# FUNCTIONS AREA
# ----------------------------------------
# login function. When program starts, this is the first function,
# where a user needs to login. A file in local storage contains a list
# of names, passwords, and access-levels. This is read in before user
# interaction begins.
        
def login(userList):
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
            
        userPasswordInput = input("Please input your password: ")
        pw = userPasswordInput.strip()
        if (userList[name]["Password"] == pw):
            print("You are logged in, " + name)
            encryptPassword(pw)
            return name
            
        else:
            print("Incorrect password. Exiting program.")
            exit()
    except KeyError:
        print("That was not a valid username. Please try again. Exiting program")
        exit()

# enterReportingArea function. Allows users to enter the lowest-level
# "Reporting" area of app

def encryptPassword(pw):
    print("Here is your password" + pw)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mixed = list(alphabet)
    random.shuffle(mixed)
    mixed = ''.join(mixed)
    print(mixed)
    

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
                areas[row["Name"]] = item
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

# MAIN EXECUTION AREA -----------------------------------

userList = {}
filename = "areas.txt"
plainWord = "cat"

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

encryptedWord = encryptWord(plainWord, randomizedAlpha)
print("Yo " + encryptedWord)
decryptWord(encryptedWord, randomizedAlpha)
print("Goodbye")
