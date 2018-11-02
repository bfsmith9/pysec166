#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# FUNCTION TO CREATE HASHES FOR PASSWORD                #
# BARRY SMITH - NOV 6, 2018                             #
#########################################################

import hashlib

def hashPassword(password, salt):
    hash = hashlib.sha512(password.encode()).hexdigest()
    hashedSalt = hashlib.sha512(salt.encode()).hexdigest()
    

