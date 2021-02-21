# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:58:06 2021

@author: conta
"""

def computingPower(a,b):
    if(b==0):
        return 1;
    power=computingPower(a, b//2)
    if(b&1==0):
        return (power*power)
    else:
        return (power*power*a)
    
    
if __name__=="__main__":
    print(computingPower(int(input()), int(input())))