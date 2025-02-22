class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for j in range(n)] for i in range(n)]
        value = 0
        if n == 1:
            return [[1]]
        for layer in range(n-1):
            for top in range(layer, n-layer):
                value += 1
                matrix[layer][top] += value
            for right in range(layer + 1, n-layer):
                value+= 1
                matrix[right][n-1-layer] += value
            for bottom in range(n-layer-2, layer-1, -1):
                value+=1
                matrix[n-layer-1][bottom] += value
            for left in range(n-layer-2,layer,-1):
                value+=1
                matrix[left][layer] += value
        return matrix