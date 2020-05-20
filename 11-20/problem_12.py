#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:05:08 2020

@author: kathykiutang
"""

# fins the first triangle number that has over 500 divisors 

# e.g. 28 has over 5 

import time

def triangle (n):
    return sum([i for i in range (1,n+1)])


start = int(round(time.time() * 1000)) # starts the stopwatch

j = 0
n = 0
divisors = 0

while divisors <= 500:
    
    divisors = 0 # reset for the next number counting
    
    j+= 1 # starts with 1
    n = triangle(j) # return the conrresponding triangle number 
    
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            divisors += 1
        i += 1
    
    divisors = divisors*2 # check the exit condition


finish = int(round(time.time() * 1000)) # stops the stopwatch

print (n)
print ("Time taken: " + str(finish-start) + " milliseconds")
    
    
    
    
    
    
    
        