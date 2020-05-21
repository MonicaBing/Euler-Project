#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:11:56 2020

@author: kathykiutang
"""

def fact (n):
    sum_value = 1
    for i in range (2,n+1):
        sum_value = sum_value*i
        
    return sum_value 

output = fact(40)/ (fact(20)*fact(20))