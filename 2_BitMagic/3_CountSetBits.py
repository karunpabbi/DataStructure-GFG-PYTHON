# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 00:06:27 2021

@author: conta
"""

def CountSetBitsNaive(n):
    res= 0
    while n>0:
        res=res+(n&1)
        n=n>>1
    print("Naive :",res)
    
def BrainKerninghamAlgorithm(n):
    # Idea is to  make last set bit off in every iteration
    res=0
    while n>0:
        n=n&(n-1)
        res+=1
    print("BrainKerningham : ",res)
    
def LookUpTableMethod(n):
    table = list(range(256))
    
    table[0]=0
    for i in range(256):
        table[i]=(i&1)+table[i>>1]
        
    res=table[n & 0xff]
    n=n>>8
    res+=table[n & 0xff]
    
    n=n>>8
    res+=table[n & 0xff]
    
    n=n>>8
    res+=table[n & 0xff]
    
    print("LookUp Table : ",res)
    
    
if __name__=="__main__":
    n=int(input())
    CountSetBitsNaive(n)
    BrainKerninghamAlgorithm(n)
    LookUpTableMethod(n)
    