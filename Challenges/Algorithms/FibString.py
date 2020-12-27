# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 02:43:42 2020

@author: win10
"""
def Fibonacci(F0, F1, Target):
    Fib = []
    if Target<=F0:
        return [F0]
    Fib = Fib + [F0, F1]
    counter = 1
    while Fib[counter] < Target:
        counter+=1
        Fib.append(Fib[counter-2] + Fib[counter-1])
    return Fib

def FindCharacterat(Search, Target, Strings):
    
    offset = Target-1       #Adjusting for index 0
    lookin = len(Search)-1  #Adjusting for index 0
    
    while lookin >1:
        
        split = Search[lookin-2]
        
        if offset < split:
            #look in the left substring
            lookin = lookin - 2
        else:
            #look in the right substring
            lookin = lookin - 1
            offset = offset-split
    
    print(Strings[lookin][offset])
    return 

if __name__ == '__main__':
    
    num_tests = int(input().strip())
    tests = []
    for i in range(num_tests):
        A, B, Target = input().rstrip().split()
        Target = int(Target)
        Fib = Fibonacci(len(A),len(B),Target)
        FindCharacterat(Fib, Target, [A,B])