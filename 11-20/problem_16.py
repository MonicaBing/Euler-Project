#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:44:38 2020

@author: kathykiutang
"""

value = str(2**1000)

output = 0

for i in range (len(value)): # 301
    output = output + int(value[i])