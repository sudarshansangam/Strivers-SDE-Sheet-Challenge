# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# SOLUTION:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # sorted(nums)
        max_len = 1
        count = 1

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        else:
            for i in range(len(nums)-1):
                if nums[i] == (nums[i+1]-1):
                    count += 1
                    max_len = max(count,max_len)
                elif nums[i] == nums[i+1]:
                    max_len = max(count,max_len)
                else:
                    count = 1
        
        return max_len