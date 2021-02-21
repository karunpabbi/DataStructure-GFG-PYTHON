# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:08:43 2021

@author: conta
"""
from math import floor,sqrt

def printDivisors(n):
    for i in range(1,floor(sqrt(n))+1):
        if(n%i==0):
            print(i)
            
            if(i!=n/i):
                print(int(n/i))
                
                
if __name__=="__main__":
    printDivisors(int(input()))