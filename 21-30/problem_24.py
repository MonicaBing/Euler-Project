#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:41:15 2020

logic : https://blog.dreamshire.com/project-euler-24-solution/
"""

import math
import numpy as np

remainder = 1000000-1
numbers = 10-1

list_number = [x for x in range(10)]

final = []

# divsion 


for i in range (9):

    division = int(np.floor((remainder)/math.factorial(numbers))) #2
    
    remainder = (remainder) % (math.factorial(numbers))
    
    final.append(list_number[division])
    
    del(list_number[division])
    
    numbers = numbers - 1


final.append(list_number[0])

