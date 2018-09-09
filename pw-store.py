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
# For each key in areas there will be an array

def printUsers(users):
 
    for key, value in users.items():
        print("Name: " + str(key))   
        print("Access Level: " + str(value["Access_Level"]))

    print()

def lookup_number(areas, name):
    if areas.has_key(name):
        return "The number is "+areas[name]
    else:
        return name+" was not found"

def remove_number(areas,name):
    if areas.has_key(name):
        del areas[name]
    else:
        print(name," was not found")
        
def enterReportingArea():
    print("You have now entered the reporting area")

#def loadUsers(areas,filename):
#    in_file = open(filename,"r")
#    while true:
#        in_line=in_file.readline()
#        if in_line == "":
#            break
#        in_line = in_line[:-1]
#        [name,pass,auth_code] = in_line.split(',')
#        areas[name[0]] = pass
#        areas[name[1]] = auth_code
#    in_file.close()

#def loadUsers(areas,filename):
#    with open(filename, 'r') as data_file:
#        data_file.next()
#        for row in data_file:
#            row = row.strip().split(",")
#            areas.setdefault(row[0],{})[row[1]] = row[2]

def loadUsers(areas,filename):
    with open(filename, 'r') as data_file:
        data = csv.DictReader(data_file, delimiter=",")
        for row in data:
            item = areas.get(row["Name"], dict())
            item[row["Password"]] = row["pass"]
            item[row["Access_Level"]] = row["number"]
            areas[row["Name"]] = item
#            row = row.strip().split(",")
#            areas.setdefault(row[0],{})[row[1]] = row[2]
    print(areas)

def saveUsers(areas,filename):
    out_file = open(filename, "w")
    for x in areas.keys():
        out_file.write(x+","+areas[x]+"\n")
    out_file.close()

def printMenu():
    print('1. Print users')
    print('2. Add a user')
    print('3. Remove a user')
    print('4. Lookup a user')
    print('5. Load users')
    print('6. Save users')
    print('7. (or 0) Menu')
    print('8. Quit')
    print()

userList = {}
menu_choice = 0
printMenu()
while menu_choice != "8":
  try:
    menu_choice = input("Type in a number (1-8, 0 for menu): ")
    if menu_choice == "1":
        printUsers(userList)
    elif menu_choice == "2":
        print("Add Name and Area")
        name = input("Name: ")
        phone = input("Area: ")
        add_number(userList,name,phone)
    elif menu_choice == "3":
        print("Remove Name and Area")
        name = input("Name: ")
        remove_number(userList,name)
    elif menu_choice == "4":
        print("Lookup Name")
        name = input("Name: ")
        print(lookup_number(userList,name))
    elif menu_choice == "5":
        filename = "areas.txt"
        loadUsers(userList,filename)
    elif menu_choice == "6":
        filename = "areas.txt"
        saveUsers(userList,filename)
    elif menu_choice == "7":
        printMenu()
    elif menu_choice == "0":
        printMenu()
    elif menu_choice == "8":
        #exit
        pass
    else:
        printMenu()
  except SyntaxError:
      print("That was not a number.")
  
print("Goodbye")
