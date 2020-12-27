# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:01:33 2020

@author: win10
"""
import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    #If k == 0, solution is 1...n
    if k == 0:
        return list(range(1,n+1))
    #no solutions are possible for below conditions 
    elif n % (2*k) != 0 or 2*k > n: 
        return [-1]
    return [(i+1)+(1 if (i//k)%2==0 else -1)*k for i in range(n)]


if __name__ == '__main__':
    n = 24
    k = 3
    X = absolutePermutation(n,k)
    print(X)
    
       
