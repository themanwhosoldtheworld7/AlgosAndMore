# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:01:39 2021
@author: Ainish
"""

#Global Definitions

N = 5
Queens = [None]*N
Board = [[0] * N for _ in range(N)]

def printBoard():
    print('Queens are placned at \n',Queens)
    board = [['-'] * N for _ in range(N)]
    for queen in Queens:
        if queen != None:
            r,c = queen[0],queen[1]
            board[r][c] = "Q"
    for row in board:
        string = ""
        for element in row:
            string = string +"  "+ element
        print(string, "\n")
    return
             
def isSafe(cell):
    r,c = cell[0], cell[1]
    if Board[r][c] == 0:
        return True
    return False

def removeQueen(Row):    
    cell = Queens[Row]
    placeQueen(cell, place = False)
    return
    
def placeQueen(cell, place = True):
    r,c = cell[0], cell[1]
    if place == True : U = 1
    else: U=-1
    for i in range(N):
        Board[r][i]+=U        
        Board[i][c]+=U        
        if r-i >=0 and c-i >= 0: Board[r-i][c-i] += U #LeftUpper
        if r+i <N and c-i >= 0: Board[r+i][c-i] += U #LeftLower
        if r-i >=0 and c+i < N: Board[r-i][c+i] += U #RightUpper
        if r+i <N and c+i < N: Board[r+i][c+i] += U #RightLower 
    return

def Solve_Next_Queen(Row):
    #Check if the board is already solved
    if Row == N: return True
        
    cell = Queens[Row]
    Queens[Row] = None
    if cell == None : col = 0
    else: col = cell[1]+1
    
    for i in range(col, N):
        cell = (Row, i)
        if isSafe(cell):
            placeQueen(cell)
            Queens[Row] = cell
            if(Solve_Next_Queen(Row+1)) : return True    
    removeQueen(Row-1)
    Solve_Next_Queen(Row-1)
    return True

Solve_Next_Queen(0)

printBoard()