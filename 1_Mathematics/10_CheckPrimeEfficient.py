# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:38:00 2021

@author: conta
"""
from math import floor,sqrt
def checkPrimeOpimized(n):
    if n==1:
        return False
    
    for i in range(2,floor(sqrt(n))) :
        if(n%i==0):
            return False
    return True


if __name__=="__main__":
    print(checkPrimeOpimized(int(input())))