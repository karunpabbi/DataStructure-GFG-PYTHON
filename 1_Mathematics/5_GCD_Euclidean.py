# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:53:11 2021

@author: conta
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:43:50 2021

@author: conta
"""

def gcdEuclidean(a,b):
 
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a



if __name__=="__main__":
    print(gcdEuclidean(int(input()), int(input())))