# pysec166
Code for assignments
## JIM EDDY'S INSTRUCTIONS FOR ASSIGNMENT 1
Assignment 1.0
Write a Python program: Create a login and menu to a company intranet system that requires users (employees) to enter a username and password in order to view a menu of options (such as Time Reporting, Accounting, IT Helpdesk, Engineering Documents, etc. ). 

Technical requirements:

- Plaintext usernames/passwords/access level stored in a csv (or text) file
- Create three different access levels (roles for different users). For example, User A should have access to all menu items ('admin' access), while User B has limited access (no Accounting or Engineering Documents), etc. 
- Once logged in the user should be able to select different menu options with a number input (for example, "press 1 for the Time Reporting area", "press 2 for the Accounting area", etc.).
- When a user enters a menu area they have access to, a simple message similar to 'You have now accessed the accounting application' is sufficient to indicate a successful demonstration of the access control (no need to build out any actual accounting functionality). Likewise, if a user does not have the appropriate access level to view a menu area, the program should display a 'You are not authorized to access this area.' message and provide an option to return them to the main menu.
- Good programming practices: Reasonable amount of error/exception handling. Must organize code into functions. Well-documented. Written in Python 3. No GUI necessary, this should be a command menu driven program.

Please submit a compressed folder containing all of the files associated with your assignment, as well as instructions for testing your program. Note: you will be adding functionality to this system in subsequent assignments, so take your time and plan out your design.

## JIM EDDY'S INSTRUCTIONS FOR ASSIGNMENT 2
Assignment 2.0

Write a Python program to simulate** a buffer overflow, then implement input validation to prevent it. There are two parts to this assignment:

1. The program should display a welcome message and prompt the user for a username. Create a buffer overflow condition by allowing a user to input more data than the size of the allocated memory (causing the program to crash). 

2. Implement input validation to mitigate the overflow vulnerability. Check that the username entered has a minimum length of 8 characters and a maximum of 25 characters. If the user enters a username length outside those limits, return an error message and prompt the user to re-enter the username. 

Please submit a compressed folder containing two python files (one for part 1, and another for part 2) associated with your assignment, as well as instructions for testing your program.

*Note: I am using Python since it is a prerequisite for this course. A language such as C would provide a real buffer overflow, thus this exercise is designed to build a conceptual understanding of the condition.*

