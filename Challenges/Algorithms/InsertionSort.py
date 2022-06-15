#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:25:34 2022

@author: ainish

Insertion Sort
"""


def insertionsort(Array):
    
    size = len(Array)
    
    for i in range(0,size-1):

        for j in range(i-1,0,-1):
            print(Array[i], Array[j])
            if Array[j]>Array[i]:
                Array[j],Array[i] = Array[i], Array[j]
            else:
                break
            
    
    return Array


Unsorted = [1,3,2,4,8,7,5,6,9]
SortedArray = insertionsort(Unsorted)