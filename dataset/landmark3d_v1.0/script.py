#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 01:18:14 2018

@author: marwan
"""

with open("list_db.txt") as f:
    with open("train1.txt", "w") as f1:
        i = 0
        for line in f:
            i=i+1
            if(i>800):
                break
            else:
                f1.write(line)                     
                
                
            
            
with open("list_test.txt") as e:
    with open("test.txt", "w") as e1:
        j = 0
        for line in e:
            j=j+1
            if(j>250):
                break
            else:
                e1.write(line) 
