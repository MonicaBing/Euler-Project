#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:36:58 2020

@author: kathykiutang
"""

with open('names.txt') as f:
    names = f.read()

    
def name_score (name):
    letters = list(name)
    letters = [ord(x)-64 for x in letters]
    return sum(letters)

names = names.strip().split(',')

a = [x[1:-1] for x in names]

a.sort()

score = 0

for i in range (len(a)):
    score += name_score(a[i])*(i+1)

print(score)