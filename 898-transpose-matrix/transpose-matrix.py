class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        width = len(matrix[0])
        height = len(matrix)
        result = [[0 for i in range(height)] for j in range(width)]
        for i in range(height):
            for j in range(width):
                result[j][i] += matrix[i][j]
        return result
        