#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:12:40 2020

@author: kathykiutang
"""

value = 2000000
sum_value = 2
count = 0

for n in range (3,value + 1): 
    for i in range (2,n):
        if n%i == 0:
            count = count +1
    if count == 0:
        sum_value = sum_value + n
    count = 0
    
    print(n)


