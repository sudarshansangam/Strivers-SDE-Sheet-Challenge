# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# SOLUTION:

from os import *
from sys import *
from collections import *
from math import *

def slidingWindowMaximum(nums:list, k:int):
	# Write your code here
	# Return a list
	res = []
	
	max_value = int(nums[0])

	if len(nums) * k == 0:
		return []

	for i in range(len(nums)-k+1):
		res.append(int(max(nums[i:i+k])))
	
	res = map(int,res)
	return res

	# for j in range
	pass

# OTHER SOLUTION:

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
	
        if len(nums) * k == 0:
            return []
        
        return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
    
# SOLUTION USING DEQUE USING ARRAY:

from os import *
from sys import *
from collections import *
from math import *

def slidingWindowMaximum(nums:list, k:int):
	# Write your code here
	# Return a list
	res = []
	
	deq = nums[:k]
	res.append(max(deq))

	for i in range(k, len(nums)):
		deq.pop(0)
		deq.append(nums[i])
		max_value = max(deq)
		res.append(max_value)

	return res