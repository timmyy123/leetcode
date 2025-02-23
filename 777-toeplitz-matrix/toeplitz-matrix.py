class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        isToeplitz = True
        for shift in range(m):
            diagonal = [matrix[i][j] for i in range(m) for j in range(n) if j+shift == i]
            for i in range(len(diagonal)-1):
                if diagonal[i] != diagonal[i+1]:
                    isToeplitz = False
        for shift in range(n):
            diagonal = [matrix[i][j] for i in range(m) for j in range(n) if i+shift == j]
            for i in range(len(diagonal)-1):
                if diagonal[i] != diagonal[i+1]:
                    isToeplitz = False
        return isToeplitz
        