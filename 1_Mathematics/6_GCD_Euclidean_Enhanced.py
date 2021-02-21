# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:59:32 2021

@author: conta
"""

def gcdEuclideanEnhanced(a,b):
    if(b==0):
        return a
    return gcdEuclideanEnhanced(b, a%b)


if __name__=="__main__":
    print(gcdEuclideanEnhanced(int(input()), int(input())))