# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:43:50 2021

@author: conta
"""

def gcdNaive(a,b):
    res=min(a,b)
    
    while(res>0):
        if(a%res==0 and b%res==0):
            break
        res-=1
    return res



if __name__=="__main__":
    print(gcdNaive(int(input()), int(input())))