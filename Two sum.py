

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