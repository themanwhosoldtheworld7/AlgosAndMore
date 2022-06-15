#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:56:02 2022

@author: ainish
"""

def mergesort(Array):
    size = len(Array)
    if size == 1:
        return Array
    
    f_Array = Array[0:int(size/2)]
    s_Array = Array[int(size/2):]
    
    f_Array = mergesort(f_Array)
    s_Array = mergesort(s_Array)
    
    return merge(f_Array, s_Array)

def merge(F_Array, S_Array):
    MergedArray = []
    
    while F_Array and S_Array:
        if F_Array[0] < S_Array[0]:
            MergedArray.append(F_Array[0])
            F_Array.pop(0)
        else:
            MergedArray.append(S_Array[0])
            S_Array.pop(0)
       
    if F_Array:
        MergedArray = MergedArray + F_Array
    else:
        MergedArray = MergedArray + S_Array
   
    return MergedArray





X = mergesort([5,6,4,7,3,8,2,9,1])

