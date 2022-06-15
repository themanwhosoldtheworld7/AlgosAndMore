"""
Created on Sun Nov 21 18:43:16 2021
@author: Ainish
"""


import timeit

def Fibonacci_Iterative(n):
    
    if n<=0: return 0
    if n<=2: return 1    
     
    fib_n1 = 1
    fib_n2 = 1
    
    for i in range (2,n):
        fib_n  = fib_n2 + fib_n1
        fib_n2 = fib_n1
        fib_n1 = fib_n
        
    return fib_n


def Fibonacci_Recursive(n):
    
    if n<=0: return 0            
    if n<=2: return 1 
    
    return Fibonacci_Recursive(n-2) + Fibonacci_Recursive(n-1)
    

def Fibonacci_DP (n, fib = {}):
    
    if n<=0: return 0    
    if n<=2: return 1
   
    try:
        if fib[n]: return fib[n]
    except:
        fib[n] = Fibonacci_DP(n-1) + Fibonacci_DP(n-2)
    return fib[n]
    

def Iterative_Time()    :
    SETUP_CODE = "from __main__  import Fibonacci_Iterative"    
    TEST_CODE  = "Fibonacci_Iterative(10)"
    
    times = timeit.repeat(
                            setup = SETUP_CODE,
                            stmt  = TEST_CODE,
                            repeat = 10,
                            number = 1000                            
                            )
    return min(times)/1000

def Recursive_Time()    :
    SETUP_CODE = "from __main__  import Fibonacci_Recursive"    
    TEST_CODE  = "Fibonacci_Recursive(10)"
    
    times = timeit.repeat(
                            setup = SETUP_CODE,
                            stmt  = TEST_CODE,
                            repeat = 10,
                            number = 1000                            
                            )
    return min(times)/1000

def DP_Time()    :
    SETUP_CODE = "from __main__  import Fibonacci_DP"
    TEST_CODE = "Fibonacci_DP(10)"
    
    times = timeit.repeat(
                            setup = SETUP_CODE,
                            stmt  = TEST_CODE,
                            repeat = 10,
                            number = 1000                            
                            )
    return min(times)/1000

def TimeComplexity(TestRange = 10):
    SETUP_CODE = ["from __main__  import Fibonacci_Iterative",
                  "from __main__  import Fibonacci_Recursive",
                  "from __main__  import Fibonacci_DP"]
    
    TEST_CODE = ["Fibonacci_Iterative",
                 "Fibonacci_Recursive",
                 "Fibonacci_DP"]
    
    
    TimeComplexity = []    
    for n in range (TestRange):
        Complexity = []
        TYPE = '(' + str(n) + ')'
        for i in range(3):            
            times = timeit.repeat(
                                    setup = SETUP_CODE[i],
                                    stmt  = TEST_CODE[i] + TYPE,
                                    repeat = 10,
                                    number = 1000                            
                                        )
            Complexity.append(min(times))
        TimeComplexity.append(Complexity)
    return TimeComplexity
    
    pass


def main():
    i = 10      
    print(Fibonacci_Iterative(i))               
    print(Fibonacci_Recursive(i))
    print(Fibonacci_DP(i))

    
    return 

if __name__ == "__main__":
    main()           
    time_Iterative = Iterative_Time()
    time_DP        = DP_Time()
    time_Recursive = Recursive_Time()
    Time = TimeComplexity(20)

    