# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 00:44:45 2021

@author: conta
"""

def OddOccuringElement(a):
    res=0
    for i in a:
        res=res^int(i)
    return res

if __name__=="__main__":
    print(OddOccuringElement(list(input().split(" "))))