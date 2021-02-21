# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:34:29 2021

@author: conta
"""

def gcdEuclideanEnhanced(a,b):
    if(b==0):
        return a
    return gcdEuclideanEnhanced(b, a%b)

def lcmOptimized(a,b):
    return int((a*b)/gcdEuclideanEnhanced(a, b))




if __name__=="__main__":
    print(lcmOptimized(int(input()), int(input())))