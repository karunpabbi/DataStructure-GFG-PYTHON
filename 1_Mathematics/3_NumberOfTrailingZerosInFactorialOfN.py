# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:45:18 2021

@author: conta
"""
from math import floor
def countNoOfZerosFactorial(n):
    res=0
    for i in range(5,n+1,5):
        print(i)
        res=res + floor(n/i)
    return res

if __name__=="__main__":
    print(countNoOfZerosFactorial(int(input())))