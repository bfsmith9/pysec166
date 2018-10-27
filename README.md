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

## JIM EDDY'S INSTRUCTIONS FOR ASSIGNMENT 5

Assignment 5.0

In this assignment, you will enhance the intranet system you created in Assignment 1.0. You will add the ability for a new user to register if they aren't already a user. You will encrypt the password they choose with your own *encryption algorithm* (no built-in hashing functions, we'll improve on this in a later assignment), and store the password ciphertext in the csv (or txt) file. You will add the functionality to decrypt the password and authenticate the user.

Technical requirements:

- Plaintext usernames, encrypted passwords, and access level stored in a csv (or txt) file.
- Add the ability for a new user to register and choose a username and password (set new user access level at your 'least privileged' level by default)
- Encrypt the password the user enters using your own encryption algorithm (not a built in hashing algorithm). A basic example (your implementation needs to be significantly more complex) would be to have the user input a password 'test' and use Python to apply an algorithm to encrypt it. The following uses string slicing to reverse the characters (so 'test' becomes 'tset')

	- password = 'test'
	- encrypted = password[::-1]
	- print(encrypted)
	- output would be 'tset' (test spelled backwards, which you would then store in the csv (or txt) file as the encrypted password. When a registered user types in their password, you need to 'reverse' your algorithm (in this example it would be password[::1] ) to change the ciphertext back into plaintext for authentication).

- Add input validation to require the password length to be a minimum of 8 characters and a maximum of 25 characters. If the user enters a password length outside those limits, return an error message and prompt the user to re-enter the password. 
- Add input validation to require the user to have at least one number and at least one letter in the password
- Reasonable amount of error handling.

Please submit a compressed folder containing all of the files associated with your assignment, as well as a description of your encryption algorithm (pseudocode) and instructions for testing your program.

## JIM EDDY'S INSTRUCTIONS FOR ASSIGNMENT 6

Assignment 6.0

### PART 1 (10%): Hashing

Generate the (hexidecimal) hash using the identified algorithm for the following passwords (apostrophes not included):

- Use md5 to generate the hash for the password: 'letMeIn'
- Use md5 to generate the hash for the password: 'admin'
- Use sha1 to generate the hash for the password: 'gr8tPW'
- Use sha256 to generate the hash for the password: 'hello123'
- Use sha512 to generate the hash for the password: 'v@ry$ecURE!'

### PART 2 (15%): Salting

- Add the salt 'cyber' to the end of the md5 hash for the password: 'helpdesk'
- Generate the md5 hash of the salt 'cyber' and add it to the end of the md5 hash for the password: 'helpdesk'
- Generate the md5 hash of the password + salt (which is 'helpdesk' concatenated with the salt 'cyber')
- Generate a pseudeo-random salt, add it to the end of the password 'helpdesk' and generate the md5 hash of the password + hash combination. Explain how you generated the pseudo-random salt.
- Respond: How does salting passwords make them more secure?

### PART 3 (75%): Cracking

Write a password cracking program in python that reads in the wordlist passwords provided here: wordlist800.txt
 and searches for the original plaintext password that matches the following (unsalted) md5 password hash: 'cc8b1415557f58abf2e2fa83c2ea6c91'

To get you started, here is the basic python to generate an md5 hash:

import hashlib
pw = 'testing'

h = hashlib.md5(pw.encode()).hexdigest()

print(h)


Submit a compressed folder of your code as well as a screenshot demonstrating you successfully cracked the password. 

