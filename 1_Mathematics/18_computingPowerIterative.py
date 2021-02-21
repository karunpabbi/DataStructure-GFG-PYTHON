# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:13:06 2021

@author: conta
"""

def iterativePower(a,b):
    res=1
    while b>0:
        if(b&1!=0):
            res*=a
        a*=a
        b=b>>1
    
    return res

if __name__=="__main__":
    print(iterativePower(int(input()), int(input())))