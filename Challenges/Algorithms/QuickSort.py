#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:14:33 2022

@author: ainish
"""

def QuickSort (Array, low, high):
    if low < high:
        pivot = Partition (Array, low, high)
        QuickSort(Array, low, pivot)
        QuickSort(Array, pivot+1, high)
        return

def Partition (Array, low, high):
    pivot = Array[low]
    left = low
    
    for i in range (low+1, high, 1):
        if Array[i] < pivot:
            Array[i], Array[left] = Array[left], Array[i]
            left+=1
    
    Array[left], pivot = pivot, Array[left]
    return left

Array = [5,6,4,7,3,8,2,9,1]
X = QuickSort(Array,100,100)