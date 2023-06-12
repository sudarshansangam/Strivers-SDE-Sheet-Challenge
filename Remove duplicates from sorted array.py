# You are given a sorted integer array' ARR' of size 'N'. You need to
#  remove the duplicates from the array such that each element
#  appears only once. Return the length of this new array.

#  Note:
#    Do not allocate extra space for another array. You
#    need to do this by modifying the given input array
#    in-place with 0(1) extra memory.

# SOLUTION:

def removeDuplicates(arr,n):
    # Write your code here.
    elements = []
    for i in arr:
        if i in elements:
            continue
        elements.append(i)
    return len(elements)
    pass
