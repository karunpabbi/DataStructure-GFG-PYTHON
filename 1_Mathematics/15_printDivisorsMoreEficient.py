# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:21:22 2021

@author: conta
"""
from math import floor,sqrt
def printDivisorsostEfficient(n):
    i=1
    for a in range(i,floor(sqrt(n))):
        if(n%a==0):
            print(a)
    for a in range(i,1):
        if(n%a==0):
            print(a)
            
if __name__=="__main__":
    printDivisorsostEfficient(int(input()))