class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size//2):
            for j in range(size//2):
                matrix[i][j], matrix[j][size-i-1], matrix[size-i-1][size-j-1], matrix[size-j-1][i] = matrix[size-j-1][i], matrix[i][j], matrix[j][size-i-1], matrix[size-i-1][size-j-1]
        if size % 2 == 1:
            i = size//2
            for j in range(size//2):
                matrix[i][j], matrix[j][size-i-1], matrix[size-i-1][size-j-1], matrix[size-j-1][i] = matrix[size-j-1][i], matrix[i][j], matrix[j][size-i-1], matrix[size-i-1][size-j-1]
        