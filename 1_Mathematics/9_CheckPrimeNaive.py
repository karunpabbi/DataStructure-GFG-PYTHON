# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:26:51 2021

@author: conta
"""

def checkPrime(n):
    
    if n==1:
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
    
if __name__=="__main__":
    print(checkPrime(int(input())))