# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 00:01:35 2021

@author: conta
"""

def CheckKthBit(a,n):
    if(a&(1<<n-1)):
        print(True)
    else:
        print(False)
        
if __name__=="__main__":
    CheckKthBit(int(input()), int(input()))