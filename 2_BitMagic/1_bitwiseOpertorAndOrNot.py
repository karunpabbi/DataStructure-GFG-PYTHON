# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:11:53 2021

@author: conta
"""

def BitwiseTest(a,b):
    print(a&b)
    print(a|b)
    print(a^b)
    
    
if __name__=="__main__":
    BitwiseTest(int(input()), int(input()))