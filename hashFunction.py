#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 7 - CS166                                  #
# FUNCTION TO CREATE HASHES FOR PASSWORD                #
# BARRY SMITH - NOV 6, 2018                             #
#########################################################

import hashlib
# from randomSalt import randomizeWord


def hashPassword(password, salt):
    # print(password)
    # print(salt)
    hashString = hashlib.sha512(password.encode()).hexdigest()
    # print(hashString)
    hashedSalt = hashlib.sha512(salt.encode()).hexdigest()
    # print(hashedSalt)
    passwordPlusSalt = hashString + hashedSalt
    # print(passwordPlusSalt)
    hashCombo = hashlib.sha512(passwordPlusSalt.encode()).hexdigest()
    # print(hashCombo)
    
    return hashCombo

# This is working
# hashPassword("dogbert", "remy")

    

