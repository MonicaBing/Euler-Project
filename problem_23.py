#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:41:15 2020

@author: kathykiutang
"""

number = [x for x in range (28123+1)] #28123

test = number

# list of deficient 

for i in range (1,len(test)): # skip 0
    print(i)
    score = 0
    for j in range (1,i): # exclude division by 0
        if test[i] % j == 0:
            score += j
        
    if score < i:
        test[i] = 0
    

# list of perfect 

for i in range (1,len(test)): # skip 0
    print(i)
    score = 0
    for j in range (1,i): # exclude division by 0
        if test[i] % j == 0:
            score += j
        
    if score == i:
        test[i] = 0
    
# sum them, 0 in the number list, remaining is abundent
abundent = test

abundent_list = list(filter(lambda a:a!=0, abundent))

original = [x for x in range (28123+1)]

for i in range (len(abundent_list)): # fix this one
    print(i)
    for j in range (len(abundent_list)):
        value = abundent_list[i] + abundent_list[j]
        
        if value > 28123:
            break
        else:
            original[value] = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        