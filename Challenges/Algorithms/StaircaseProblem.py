"""
https://www.dailycodingproblem.com/
https://www.dailycodingproblem.com/blog/staircase-problem/

There's a staircase with N steps, and you can climb 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.
"""

   


def Staircase(n, fib = {}):
    """Starting conditions and constraints"""
    if n<0: return 0    
    if n<=1: return 1   
   
    try:
        if fib[n]: return fib[n]
    
    except:
        fib[n] = Staircase(n-1) + Staircase(n-2)
    return fib[n]


def gen_staircase(steps,n, fib = {}, is_sorted = False):    
    
    if is_sorted == False:
        steps.sort()
        is_sorted = True
        
    """Check if already calculated"""    
    try:
        if fib[n]: return fib[n]
    
    except:    
        """ Case when the stair is lower than the lowest number of permissible step """
        if n < steps[0]: return 0
        
        """ Number of ways we can get to step n = sum of ways we can get to each previous step (ie n-step)"""
        fib[n] = 0        
        for step in steps:
            fib[n] = fib[n] + gen_staircase(steps, n-step) 
            
        """Adjusting for when one can also get to step n as their first step"""
        if n in steps:
            fib[n] = fib[n]+1        
        
    return fib[n]
    
    


    