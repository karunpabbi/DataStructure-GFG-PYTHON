# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:30:47 2021

@author: conta
"""
from math import floor,sqrt

def getPrimeFactors(n):
    if n<=1:
        return 
    
    while(n%2==0):
            print(2)
            n=n/2
            
    while(n%3==0):
            print(3)
            n=n/3
    
    for i in range(5,floor(sqrt(n))+1,6):
        while(n%i==0):
            print(i)
            n=n/i
        while(n%(i+2)==0):
            print(i+2)
            n=n/(i+2)
    


    if n>3:
        print(n)
                
                
if __name__=="__main__":
    getPrimeFactors(int(input()))
            