#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:50:18 2020

@author: kathykiutang

PLEASE remember everything in here, ignore the first cell, a[1] = 1st, a[0] = none

"""

def month30(from_end):
    
    """
    return the days from the month end, index of all the sundays
    """
    
    count = 0
    
    temp_month = [0]*(30+1)

    from_start = 7-from_end

    for n in range (0,int((30-from_start)/7)+1): # include itself
        temp_month[from_start+n*7] = 1

    index = [index for index in range(len(temp_month)) if temp_month[index] == 1]

    from_end = (len(temp_month)-1) - index[-1]
    
    if index[0] == 1:
        count = 1
    
    return from_end,count

def month31(from_end): 
    
    count = 0
      
    temp_month = [0]*(31+1)

    from_start = 7-from_end

    for n in range (0,int((31-from_start)/7)+1): # include itself
        temp_month[from_start+n*7] = 1

    index = [index for index in range(len(temp_month)) if temp_month[index] == 1]

    from_end = (len(temp_month)-1) - index[-1]
    
    if index[0] == 1:
        count = 1
    
    return from_end,count


def month28(from_end): 
    
    count = 0
    
    temp_month = [0]*(28+1)

    from_start = 7-from_end

    for n in range (0,int((28-from_start)/7)+1): # include itself
        temp_month[from_start+n*7] = 1

    index = [index for index in range(len(temp_month)) if temp_month[index] == 1]

    from_end = (len(temp_month)-1) - index[-1]
    
    if index[0] == 1:
        count = 1
    
    return from_end,count

def month29(from_end):
    
    count = 0
    
    temp_month = [0]*(29+1)

    from_start = 7-from_end

    for n in range (0,int((29-from_start)/7)+1): # include itself
        temp_month[from_start+n*7] = 1

    index = [index for index in range(len(temp_month)) if temp_month[index] == 1]

    from_end = (len(temp_month)-1) - index[-1]
    
    if index[0] == 1:
        count = 1
    
    return from_end, count

"""
1 Jan 1900 - 31 Dec 1900 initilisation

"""
year = 1900 

jan_1900 = [0]*(31+1) 

for n in range (1,int(31/7)+1):
    jan_1900[n*7] = 1 

index_jan = [index for index in range(len(jan_1900)) if jan_1900[index] == 1]

from_end_jan = (len(jan_1900)-1) - index_jan[-1] 


if year%100 == 0: # it is a century
    if year % 400 == 0:
        from_end_feb,count2 = month29(from_end_jan)
    else:
        from_end_feb,count2 = month28(from_end_jan)
else: # not a century, just a normal year
    if year % 4 == 0:
        from_end_feb,count2 = month29(from_end_jan)
    else:
        from_end_feb,count2 = month28(from_end_jan)
    
from_end_march,count3 = month31(from_end_feb)
from_end_april,count4 = month30(from_end_march)
from_end_may, count5 = month31(from_end_april)
from_end_june,count6 = month30(from_end_may)
from_end_july,count7 = month31(from_end_june)
from_end_aug,count8 = month31(from_end_july)
from_end_sep,count9 = month30(from_end_aug)
from_end_oct,count10 = month31(from_end_sep)
from_end_nov,count11 = month30(from_end_oct)
from_end_dec,count12 = month31(from_end_nov)

"""
1901 onwards, only start counting here
"""

count = []
for i in range (1901,2001):
    year =i # 1901 
    
    from_end_jan,count1 = month31(from_end_dec) # 1901 
    
    if year%100 == 0: # it is a century
        if year % 400 == 0:
            # 29
            from_end_feb, count2 = month29(from_end_jan)
        else:
            #28
            from_end_feb,count2 = month28(from_end_jan)
    else: # not a century, just a normal year
        if year % 4 == 0:
            from_end_feb,count2 = month29(from_end_jan)
        else:
            from_end_feb,count2 = month28(from_end_jan)
        
    from_end_march,count3 = month31(from_end_feb)
    from_end_april,count4 = month30(from_end_march)
    from_end_may,count5 = month31(from_end_april)
    from_end_june,count6 = month30(from_end_may)
    from_end_july,count7 = month31(from_end_june)
    from_end_aug,count8 = month31(from_end_july)
    from_end_sep,count9 = month30(from_end_aug)
    from_end_oct,count10 = month31(from_end_sep)
    from_end_nov,count11 = month30(from_end_oct)
    from_end_dec,count12 = month31(from_end_nov)
    
    count.append(count1 + count2 + count3+ count4 + count5 + count6 + count7 + count8 + \
                 count9+ count10+ count11 + count12)

print(sum(count))


