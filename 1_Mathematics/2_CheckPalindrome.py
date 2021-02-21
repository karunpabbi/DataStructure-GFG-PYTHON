# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:31:39 2021

@author: conta
"""

def findPalindrome(s):
    ssize=len(s)    
    for i in range(ssize):
        if(i <= ssize/2):
            if(s[i]==s[ssize-1-i]):
                continue
            else:
                return "Not a palindrome"
                break
    return "Palindrome"
            
            
if __name__=="__main__":
    print(findPalindrome(input()))
                