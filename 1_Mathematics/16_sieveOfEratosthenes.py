# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:18:27 2021

@author: conta
"""

from math import floor,sqrt


def seiveOfEratosthenes(n):
    mark=[True]*(n+1)
    mark[0]=False
    for i in range(2,floor(sqrt(n)+1)):
        
        if(mark[i]):
            print(i)
            for j in range(i*i,n+1,i):
                mark[j]=False
        
            for i in range(2,n+1):
                if(mark[i]):
                    print(i,end=" ")
                else:
                    print(" ",end=" ")
            print()
         
     
     
    
if __name__=="__main__":
    seiveOfEratosthenes(int(input()))