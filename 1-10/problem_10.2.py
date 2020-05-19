#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:42:29 2020

@author: kathykiutang
"""

def isPrime (n):
    """
    check is the number is prime number
    """
    for i in range (2,n):
        if n % i == 0:
            return False 
    return True

total = 2
value = 2000000

for i in range (3,value):
    if isPrime(i): # if it is a prime number
        print(i)
        total = total + i
        
        
    