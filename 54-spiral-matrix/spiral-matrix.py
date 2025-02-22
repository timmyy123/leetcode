class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        layers = 0
        width = len(matrix[0])
        height = len(matrix)
        result = []
        while True:
            if layers * 2 < width:
                result += matrix[layers][layers: width-layers]
            else:
                break
            if layers * 2 + 1 < height:
                result += [matrix[row][width-layers-1] for row in range(layers+1, height - layers)]
            else:
                break 
            if layers * 2 + 1 < width:
                result += matrix[height-layers-1][width-layers-2:(layers-1) if (layers-1) >= 0 else None :-1]
            else:
                break
            if layers * 2 + 2 < height:
                result += [matrix[row][layers] for row in range(height - layers - 2,  layers, -1)]
            else:
                break
            layers += 1
        return result
            



        