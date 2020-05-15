#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:34:51 2020

@author: kathykiutang
"""

# find the divisble ones 

divisble = []

value = 600851475143
test_value = 13195

for i in range (2,value+1):
        if test_value % i == 0 :
            divisble.append(i)
        print(i)
        
print('finish part 1')
# check if it is primes number 

prime = []

for i in range (len(divisble)): # 15
    cond = True
    for n in range (2,divisble[i]): # 5
        if divisble[i] % n == 0:
            cond = False
    if cond:
        prime.append(divisble[i])
    print(i)
    
print('finish part2')