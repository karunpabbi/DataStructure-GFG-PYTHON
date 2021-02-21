# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:55:05 2021

@author: conta
"""
from math import log10,floor

def findDigitsIterative(a):
    count=0;
    while(a!=0):
        a=a/10;
        count+=1;
    return count;

def findDigitsRecursive(a):
    if(a==0):
        return 0;
    return 1+findDigitsRecursive(a/10);

def findDigitsOptimized(a):
    return floor(log10(a))+1;


if __name__=="__main__":
    print(findDigitsIterative(int(input())));
    print(findDigitsRecursive(int(input())));
    print(findDigitsOptimized(int(input())));