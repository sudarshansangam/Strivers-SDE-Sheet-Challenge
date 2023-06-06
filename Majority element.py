# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# SOLUTION:

from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# Write your code here.
	for i in arr:
		if arr.count(i) > (n/2):
			return i
	return -1

# USING DICTIONARY:

def findMajorityElement(arr, n):
	# Write your code here.
	# for i in arr:
	# 	if arr.count(i) > (n/2):
	# 		return i
	count = {}
	for i in arr:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	
	for i in count:
		if count[i] > (n/2):
			return i
	return -1

# ANOTHER SOLUTION:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        voter = nums[0]
        votecount=1
        for i in range(1,len(nums)):
            if voter==nums[i]:
                votecount+=1
            else:
                votecount-=1
            if votecount==0:
                voter=nums[i]
                votecount=1
        return voter