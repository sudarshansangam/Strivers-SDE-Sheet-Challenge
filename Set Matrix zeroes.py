# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Solution:

def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        row.append(j)
                    matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in row:
                    matrix[i][j] = 0