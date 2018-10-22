#! /usr/bin/env python3

#########################################################
# ASSIGNMENT 5 - CS166                                  #
# PROGRAM TO MANAGE PASSWORDS & ACCESS LEVELS FOR USERS #
# BARRY SMITH - SEPT 11, 2018                           #
#########################################################



import random

def encryptPassword(pw):
    print("Here is your password" + pw)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mixed = list(alphabet)
    random.shuffle(mixed)
    mixed = ''.join(mixed)
    print(mixed)