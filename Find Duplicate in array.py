#  You are given an array of integers 'ARR' containing N elements.
#  Each integer is in the range [1, N-1], with exactly one element
#  repeated in the array.

#  Your task is to find the duplicate element. The duplicate element
#  may be repeated more than twice in the error, but there will be
#  exactly one element that is repeated in the array.

#  Note:
#    All the integers in the array appear only once except
#    for precisely one integer which appears two or more
#    times.

# Sample input Т.
# 1
# 3
# 112

# Sample Output 1:
# 1

# Explanation of Sample Input 1:
# 1 is repeated in the array, hence function returns 1.

# Solution:

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    l = []
    for i in arr:
        if i in l:
            return i
        l.append(i) 
    pass