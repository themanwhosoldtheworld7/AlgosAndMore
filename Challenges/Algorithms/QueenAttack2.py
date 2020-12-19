# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:54:08 2020

@author: win10
"""



def DefineEdges(n,Row, Col):
    Sum = Row + Col
    n = n+1
    Diff = Row - Col
    RE = [n,Col]  #Right Edge
    LE = [0, Col] #Left Edge
    TE = [Row, n] #Top Edge
    BE = [Row,0] #Bottom Edge
   
    if Sum <= n:
        LDTE = [Sum,0] #Left Diagonal Top Edge
        LDBE = [0,Sum] #Left Diagonal Bottom Edge
    else:
        LDBE = [Sum-n,n] #Left Diagonal Top Edge
        LDTE = [n,Sum-n] #Left Diagonal Bottom Edge
   
    if Diff <= 0:
        RDTE = [0,-Diff]  #Right Diagonal Top Edge
        RDBE = [n+Diff,n] #Right Diagonal Bottom Edge
    else:
        RDTE = [n,n-Diff] #Right Diagonal Top Edge
        RDBE = [Diff,0]   #Right Diagonal Bottom Edge
   
    return [RE,LE,TE,BE,LDTE,LDBE,RDTE,RDBE]
 
   
   
def queensAttack(n, k, r_q, c_q, obstacles):
   
    dist = lambda A,B: max(abs(A[0]-B[0])-1,abs(A[1]-B[1])-1)
   
    RowQ ,ColQ = r_q, c_q
    Sum,Diff = RowQ + ColQ, RowQ - ColQ
    Q = [RowQ,ColQ]
    Edges = DefineEdges(n, RowQ, ColQ)
    obstacles = obstacles + Edges
    L,R,T,B,LDT,LDB,RDT,RDB = n,n,n,n,n,n,n,n #Queens Freedom to move
   
    for O in obstacles:
        Row,Col = O[0],O[1]

        if Col == ColQ:
            if Row > RowQ:                  
                D = dist(Q,O)
                if T>D:
                    T = D           
            else:
                D = dist(Q,O)
                if B > D:
                    B = D
       
        elif Row == RowQ:  
            #Check Row
            if Col > ColQ:
                D = dist(Q,O)
                if R > D:
                    R = D
            else:
                D = dist(Q,O)
                if L > D:
                    L = D
       
        elif Row + Col == Sum:  
            #Check Right Diagonal
            if Col > ColQ:
                D = dist(Q,O)
                if LDB>D:
                    LDB = D                    
            else:
                D = dist(Q,O)
                if LDT > D:
                   LDT = D

               
        elif Row - Col == Diff:  
            #Check Right Diagonal
            if Col > ColQ:
                D = dist(Q,O)
                if RDT > D:
                    RDT = D
            else:
                D = dist(Q,O)
                if RDB > D:
                    RDB = D   
                    
    Moves = L+ R + T+ B + LDT + LDB + RDT + RDB
    return Moves
         
print(queensAttack(10,2,1,1,[[2,2],[3,4]]))


