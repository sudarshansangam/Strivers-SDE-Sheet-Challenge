# You are given an array of size 'N'. The elements of the array are in
#  the range from 1 to 'N'.
#  Ideally, the array should contain elements from 1 to 'N'. But due to
#  some miscalculations, there is a number R in the range [1, N]
#  which appears in the array twice and another number M in the
#  range [1, N] which is missing from the array.
#  Your task is to find the missing number (M) and the repeating
#  number (R).



# SOLUTION:

from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here
    arr.sort()
    d = []
    repeat = 0
    missing = 0

    for i in range(len(arr)-1,-1,-1):
        if arr[i] in d:
            repeat = arr[i]
        else:
            d.append(arr[i])
    
    new= []
    for i in range(len(arr)):
        new.append(i+1)
    
    for i in range(len(arr)):
        if arr[i] in new:
            new.remove(arr[i])
    
    missing = new[0]
        
    return missing, repeat
    pass
