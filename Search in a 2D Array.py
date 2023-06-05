

Solution:

def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == target:
                return True
    return False
