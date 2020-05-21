#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:37:49 2020

@author: kathykiutang
"""

# dictionary for starting value: iterations
dic = {n: 0 for n in range(1,1000000)}

#initilisation
dic[1] = 1
dic[2] = 2

for n in range(3,1000000,1):
    counter = 0
    original_number = n # original starting number 
    
    while n> 1:
        
        # check if this iteration has done before, when it converges
        if n < original_number: 
            dic[original_number] = dic[n] + counter 
            break
        if n% 2 == 0:
            n = n/2
            counter += 1
        else:
            n = 3*n + 1
            counter += 1
            
values_list= list(dic.values())
keys_list= list(dic.keys())

keys_list[values_list.index(max(values_list))]


