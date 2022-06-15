#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:24:36 2022

@author: ainish
"""


def cutTheSticks(arr):
    count=[]
    arr.sort()
    count.append(len(arr))
    for i in range (1, len(arr)):
        if arr[i]!=arr[i-1]:
            count.append(len(arr)-i)
    return count

arr = [1,1,1,1,1,1,1]
a = cutTheSticks(arr)
