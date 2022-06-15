#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:48:26 2022

@author: ainish
"""

    
    
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, element):
        if self.root == None:
            self.root = Node(element)
            return
        
        current = self.root
        
        while current:
            prev = current
            
            if current.val > element:
                current = current.left
            
            elif current.val < element:
                current = current.right
            
            else:
                return
        
        if prev.val > element:
            prev.left = Node(element)
            return
        prev.right = Node(element)
        
        return
    
    def Search(self, element):
        current = self.root
        while current:
            if current.val == element:
                return ('Found')
            if current.val > element:
                current = current.left
            else:
                current = current.right
        return('Not Found')
    
    def TraverseInOrder(self):
        self.InOrder(self.root)
        
    def InOrder(self,current):
        if current:
            self.InOrder(current.left)
            print(current.val)
            self.InOrder(current.right)
            
            
    def TraversePreOrder(self):
        self.PreOrder(self.root)
        
    def PreOrder(self,current):
        if current:
            print(current.val)
            self.PreOrder(current.left)
            self.PreOrder(current.right)

    def TraversePostOrder(self):
        self.PostOrder(self.root)
        
    def PostOrder(self,current):
        if current:
            self.PostOrder(current.right)
            self.PostOrder(current.left)
            print(current.val)


        


Elements = [1,5,9,13,2,6,10,14,3,7,11,15,1,1,1,1]
A = Tree()

for Element in Elements:
    A.insert(Element)

A.TraverseInOrder()
#A.TraversePostOrder()