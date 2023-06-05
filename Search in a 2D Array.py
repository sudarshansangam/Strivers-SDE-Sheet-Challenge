#  You have been given a 2-D array "MAT" of size M X N where 'M'
#  and 'N' denote the number of rows and columns, respectively. The
#  elements of each row are sorted in non-decreasing order.
#  Moreover, the first element of a row is greater than the last
#  element of the previous row (if it exists).

#  You are given an integer 'TARGET,' and your task is to find if it
#  exists in the given 'MAT' or not.

#  Example:
#    Input: 'M' = 3, 'N' = 4, 'mat' = [[1, 2, 3, 4], [5,
#    6, 7, 8], [9, 10, 11, 12]], 'target' = 8
#    Output:

# Solution:

from typing import List

def searchMatrix(mat: List[List[int]], target: int) -> bool:
    # Write your code here.
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == target:
                return True
    return False
