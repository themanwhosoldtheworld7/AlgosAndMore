#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 08:19:42 2022

@author: ainish

Binary search
"""
import random as rn
def binarysearch(Array, Left, Right, Element):
    Pointer = 0
    if Left>=Right:
        return 'Not Found'
    
    Pointer = (Left + Right)/2
    Pointer = int(Pointer)
    
    if Array[Pointer] == Element:
        return 'Found at '+ str(Pointer)
    
    if Array[Pointer] > Element:
        """ Look in the left half """
        return binarysearch(Array, Left, Pointer, Element)
    else:
        return binarysearch(Array, Pointer+1, Right, Element)
    
    #return 'Not Found'

Array = [1,2,3,4,5,6,7,8,9,10]

for i in range(-5,15):
    search = rn.randint(1,25)
    Status = binarysearch(Array, 0, len(Array), search)
    print(search,Status)
    