#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:12:50 2020

@author: kathykiutang
"""

import math

n = math.factorial(100)

string = str(n)

result = 0

for i in range (len(string)):
    result += int(string[i])