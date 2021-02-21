# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:29:23 2021

@author: conta
"""

def lcmNaive(a,b):
    res=max(a, b)
    
    while(True):
        if(res%a==0 and res%b==0):
            break
        else:
            res+=1
    return res

if __name__=="__main__":
    print(lcmNaive(int(input()), int(input())))