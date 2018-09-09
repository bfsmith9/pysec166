#! /usr/bin/env python3

# ASSIGNMENT 1 - CS166
# PROGRAM TO MANAGE PASSWORDS & ACCESS LEVELS FOR USERS
# BARRY SMITH - SEPT 6, 2018

# STRATEGY - WHAT KIND OF DATA STRUCTURE?
# Name is key to two items: pass, level.
# areas is name of dictionary
# areas->john is showing the key "john" in areas the areas dictionary.
# john can point to the word "pass," which has "123" as its value, and to the word "level," which has 4 as its value.

# So what is it? It's one dictionary, with keys that have person's names. Each name contains 2 items: 2 keys and their associated values, so each name has an add'l dictionary associated with it.
# Or is it: areas: name->john, pass->bar, level->2???????
# vs array: array: array[0]->john, [1]->bar, [2]->2????? So that's all sort of "one thing..." Not at all what I have above.

import string
import csv
#from collections import defaultdict

true = 1
false = 0

# areas is the dictionary - top level


        
def login(userList):
    filename = "areas.txt"
    loadUsers(userList, filename)
    # How to input with spaces after name?
    name = input("Please input your name: ")
    pw = input("Please input your password: ")
    if (userList[name]["Password"] == pw):
        print("You are logged in, " + name)
        return name
    else:
        print("Incorrect password. Exiting program.")
        exit()


def enterReportingArea(name, users):
    if ((users[name]["Access_Level"] == "1") or (users[name]["Access_Level"] == "2") or (users[name]["Access_Level"] == "3")):
        print ("You have now entered the Reporting application.")
    else:
        print("You do not have permission to use this application.")
        
def enterDevelopmentArea(name, users):
    if ((users[name]["Access_Level"] == "1") or (users[name]["Access_Level"] == "2")):
        print ("You have now entered the Devlopment application.")
    else:
        print("You do not have permission to use this application.")
    
def enterFinanceArea(name, users):
    if (users[name]["Access_Level"] == "1"):
        print ("You have now entered the Finance application.")
    else:
        print("You do not have permission to use this application.")

def loadUsers(areas,filename):
    with open(filename, 'r') as data_file:
        data = csv.DictReader(data_file, delimiter=",")
        for row in data:
            item = areas.get(row["Name"], dict())
            item[row["Password"]] = row["pass"]
            item[row["Access_Level"]] = row["number"]
            areas[row["Name"]] = item


def printMenu():
    print('1. Menu')
    print('2. Enter Reporting Application')
    print('3. Enter Development Application')
    print('4. Enter Finance Application')
    print('8. Quit')

    print()

userList = {}
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
  
print("Goodbye")
