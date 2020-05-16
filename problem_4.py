#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:11:49 2020

@author: kathykiutang
"""

import numpy as np

# find all the possible combinations within limit 

lower_limit = 100
upper_limit = 999

list = []

def check(value):
    value = str(value) # benchmark
    reverse_string = []
    for i in range (len(value)): #4
            # do the reverse in here 
        reverse_string.append(value[(len(value)-1)-i]) # works
        
            
    length = len(reverse_string)
        
    reverse_value = ""
    
    if length % 2 == 0: # even number 
        for i in range (0,length,2): # 4
            reverse_value = reverse_value + str(reverse_string[i]) + str(reverse_string[i+1])
                
    else: # odd number
        even_value = length - 1
        for i in range (0,even_value,2):
            reverse_value = reverse_value + str(reverse_string[i]) + str(reverse_string[i+1])
        reverse_value = reverse_value + str(reverse_string[-1])

    if reverse_value == value:
        return True 
    else:
        return False



for i in range (lower_limit, upper_limit +1, 1): # for one 2 digits 
    for j in range (lower_limit, upper_limit+1, 1): # for another 2 digits
        mul = i*j
        if check(mul):
            list.append([mul])

print(max(list))

    
        
