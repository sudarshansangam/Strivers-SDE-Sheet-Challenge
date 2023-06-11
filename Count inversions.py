# For a given integer array/list 'ARR' of size 'N' containing all distinct
# values, find the total number of 'Inversions' that may exist.
# An inversion is defined for a pair of integers in the array/list when
# the following two conditions are met.

#    A pair ('ARR[i]', 'ARR[j]') is said to be an
#     inversion when:
#    1. 'ARR[i] > 'ARR[j]'
#    ف < 'i' 2.
#    Where 'i' and 'j' denote the indices ranging from [0,
#     'N').

# Sample Input 1 :
# 3
# 3 2 1
# Sample Output 1 :
# 3
# Explanation Of Sample Output 1:
# We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).

# Sample Input 2 :
# 5
# 2 5 1 3 4
# Sample Output 2 :
# 4
# Explanation Of Sample Output 1:
# We have a total of 4 pairs which satisfy the condition of inversion. (2, 1), (5, 1), (5, 3) and (5, 4).

# SOLUION:

def getInversions(arr, n) :
	# Write your code here.
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count