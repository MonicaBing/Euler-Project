#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:18:02 2020

@author: kathykiutang
"""

import math

def function(n):

    max_div = math.ceil(n/2)
    
    divisor = []
    for i in range (1,max_div+1):
        if n%i == 0:
            divisor.append(i)
    return sum(divisor)



result = 0

for i in range (1,10000):
    result1 = function(i) # 
    result2 = function(result1)
    
    if (i != result1) & (i == result2) & (result1 != 1): # i = 9
        result += result1 + result2
        
final_result = result/2

