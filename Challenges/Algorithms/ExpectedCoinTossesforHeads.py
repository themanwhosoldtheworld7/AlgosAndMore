#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 08:10:42 2022

@author: ainish
"""
import random
from statistics import mean

def CoinToss():
    return int(round(random.random()))

def Experiment(Heads, Trials = 1000):
    
    Results = []
    for i in range(Trials):
        Success = False
        Tosses = 0
        Run = 0
        while Success == False:
            Toss = CoinToss()
            Tosses += 1
            Run = Run+1 if Toss == 1 else 0
            Success = Run == Heads
        Results.append(Tosses)
    return mean(Results)

#Running for valrious values
Experiments = []
for i in range(10):
    Experiments.append((i, round(Experiment(i))))
    
print(Experiments)
    
    