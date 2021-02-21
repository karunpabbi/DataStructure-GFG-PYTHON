# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:38:00 2021

@author: conta
"""
from math import floor,sqrt
def checkPrimeOpimized(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    
    for i in range(5,floor(sqrt(n)),6) :
        if(n%i==0 or n%(i+2)==0):
            return False
    return True


if __name__=="__main__":
    print(checkPrimeOpimized(int(input())))