Given an array of integers arr and an integer target, return the pairs that sum up to the target given 

Example 1
Input: arr = 2 7 11 13, target = 9
Output: (2,7)

Example 2
Input: arr = 1 -1 -1 2 2, target = 1
Output: (-1,2), (-1,2)

Example 3
Input: arr = 1 -1 -1 2 2, target = 10
Output: (-1,-1)

# SOLUTION

def twoSum(arr, target, n):
    # Write your code here.
    arr = sorted(arr)
    res = []

    s = 0
    e = n - 1

    while s < e:
        if arr[s]+arr[e] > target:
            e-=1
        elif arr[s]+arr[e] < target:
            s+=1
        else:
            temp = []
            temp.append(arr[s])
            temp.append(arr[e])
            res.append(temp)
            s += 1
            e -= 1
    
    if len(res) < 1:
        res.append([-1,-1])
    return res