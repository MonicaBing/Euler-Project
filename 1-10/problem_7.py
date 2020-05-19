#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:14:09 2020

@author: kathykiutang
"""

"""
test each number if it is prime numebr, stop at the desire position. 

dont save it, to optimise it

"""        
    
number = 3
prime_count = 1
count = 0
condition = True 

while condition == True:
    for i in range (2,number):
        if number % i == 0:
            count = count + 1
            break
        
    if count == 0:  # cannot be divided
        prime_count = prime_count + 1
        print(prime_count)
    
    if prime_count == 10001 : #change the exit condition here
        condition = False
    else:
        number = number+ 1
        count = 0
        