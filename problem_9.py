#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:00:50 2020

@author: kathykiutang
"""


    
for a in range (500):
    for b in range (500):
        c = (1000 - a) - b
        if a < b < c:
            if a**2 + b**2 == c**2:
                product = a*b*c
            
                    