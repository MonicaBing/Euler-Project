#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:35:04 2020

@author: kathykiutang
"""

num = 2520 # already know that its above this 
i = 2 # anythign divided by 1 is constant 

while i < 21:
    if num % i == 0:
        i = i + 1
    else:
        num = num + 1
        i = 2

print(num)