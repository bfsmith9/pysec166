#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 5 - CS166                                  #
# ADD ENCRYPTION TO INTRANET PROGRAM                    #
# BARRY SMITH - OCTOBER 23, 2018                        #
#########################################################


import csv
import random
#from randomizeAlpha import encryptedWord

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
        
def login(userList, randomizedAlpha):
    # At first, userList is a blank dictionary
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
            userList[name] = {}
            userList[name]["Password"] = newUserPasswordInput.strip()
            userList[name]["Access_Level"] = "1"
            pw = newUserPasswordInput.strip()
            encryptWord(pw, randomizedAlpha)
            
            
            line = name + ",Password," + pw + ",Access_Level,1 "
            print(line)
            with open(filename, 'a') as data_file:
            
                data_file.write(line)
                data_file.write('\n')
            
            
            
            
            
    # except FileNotFoundError:
    #     print("File not found! Please check your directory for the {} file.".format(filename))
    #    print("Program terminating.")
    #    exit()
            
            
            
        userPasswordInput = input("Please input your password: ")
        pw = userPasswordInput.strip()
        
        
        
        
        
        
        
        if (userList[name]["Password"] == pw):
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
                print(areas.keys())
    
    except FileNotFoundError:
        print("File not found! Please check your directory for the {} file.".format(filename))
        print("Program terminating.")
        exit()

def loadUsers2(areas,filename):
    try:
        with open(filename, 'r') as data_file:
            data = csv.DictReader(data_file, delimiter=",")
            for row in data:
                print(row["No"], row["Name"], row["Password"], row["Access_Level"])
                #areas{"No"}
            if "john" in data:
                print("yes")
            else:
                print("no")    
                
    except FileNotFoundError:
        print("File not found! Please check your directory for the {} file.".format(filename))
        print("Program terminating.")
        exit()
        
def addUsers(areas2, filename):
    
    try:
        with open(filename, 'a') as data_file:
            #data = csv.DictWriter(data_file, fieldnames=fieldnames, delimiter=",")
            csvwriter = csv.writer(data_file, delimiter = ',')
            
            for row in areas2:
                #Scsvwriter.writerow(row, areas2[row]["Password"], areas2[row]["Access_Level"])
                for subrow in row:
                    csvwriter.writerows(row["Password"])


    except FileNotFoundError:
        print("File not found! Please check your directory for the {} file.".format(filename))
        print("Program terminating.")
        exit()

def addUsers2(areas2, filename):
    
    try:
        with open(filename, 'a') as data_file:
            #data = csv.DictWriter(data_file, fieldnames=fieldnames, delimiter=",")
            #csvwriter = csv.writer(data_file, delimiter = ',')
            fields = ['Name', 'Password', 'pass', 'Access_Level', 'number']
            data = csv.DictWriter(data_file, fields)

            
            for key in areas2:
                #Scsvwriter.writerow(row, areas2[row]["Password"], areas2[row]["Access_Level"])
                #for row in {'Name': key}
                #data.writerow(row["Password"])
                #row = {'Name': key}
                #row.update(val)
                #data.writerow(row)
                #data.writeheader()
                data.writerow({field: areas2[key].get(field) or key for field in fields})
    except FileNotFoundError:
        print("File not found! Please check your directory for the {} file.".format(filename))
        print("Program terminating.")
        exit()

def addUsers3(filename):
    
    line = "newname,Password,newpass,Access_Level,newnumber"
    try:
        with open(filename, 'a') as data_file:
            
            data_file.write(line)
            data_file.write('\n')
            
            
            
            
            
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

# Create a userList dictionary - empty at first
userList = {}
filename = "areas.txt"
plainWord = "cat"

print("Welcome!")
name = login(userList,randomizedAlpha)
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

#newNames = ["helen"]
#newPasswords = ["bonhomme"]
#newLevels = ["2"]

#fieldnames = ['Name', 'Password', 'Access_Level']
#addUsers(newNames, newPasswords, newLevels, filename)
filename2 = "newareas.txt"
userList2 = {'jamie': {'Password':'luigi333', 'Access_Level':'2'}}
addUsers3(filename2)

print("Goodbye")
