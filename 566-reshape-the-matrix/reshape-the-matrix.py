class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]) or (r == len(mat) and c ==len(mat[0])):
            return mat
        flat_list = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
        return [[i for i in flat_list[j*c: j*c+c]] for j in range(r)]
        