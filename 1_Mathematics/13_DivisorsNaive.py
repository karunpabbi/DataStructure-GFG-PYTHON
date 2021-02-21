# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:01:17 2021

@author: conta
"""

def printDivisors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
            
            
if __name__=="__main__":
    printDivisors(int(input()))