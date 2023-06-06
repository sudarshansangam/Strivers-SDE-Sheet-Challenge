# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]

# Example 2:

# Input: nums = [1]
# Output: [1]

# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

# SOLUTION:

from math import *
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	# Write your code here.
	count = {}
	res = []
	for i in arr:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	
	for i in count:
		if count[i] > (len(arr)/3):
			res.append(i)
	
	return res