# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 00:40:07 2021

@author: conta
"""

def CheckNoIsPowerOfTwo(n):
    if n==0:
        return "False"
        
    return(n&(n-1)==0)


if __name__=="__main__":
    print(CheckNoIsPowerOfTwo(int(input())))