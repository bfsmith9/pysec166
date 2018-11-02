#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# FUNCTION TO CREATE HASHES FOR PASSWORD                #
# BARRY SMITH - NOV 6, 2018                             #
#########################################################

import hashlib

def hashPassword(password, salt):
    print(password)
    print(salt)
    hash = hashlib.sha512(password.encode()).hexdigest()
    print(hash)
    hashedSalt = hashlib.sha512(salt.encode()).hexdigest()
    print(hashedSalt)
    passwordPlusSalt = hash + hashedSalt
    print(passwordPlusSalt)
    hashCombo = hashlib.sha512(passwordPlusSalt.encode()).hexdigest()
    print(hashCombo)
    
    return hashCombo

# This is working
# hashPassword("dogbert", "remy")

    

