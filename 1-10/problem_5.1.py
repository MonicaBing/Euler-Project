#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:13:05 2020

@author: kathykiutang
"""

#2520 

value = 1
cond = True # initial conndition
count = 0

while cond == True:
    print(value)
    for i in range (1,21,1): # 1- 10 
        if value % i == 0:
            count += 1
        else:
            break
            
    
    if count == 20:
        cond = False # exit condition 
    else:
        value += 1 # until it is right
        count = 0
        
    
232792560