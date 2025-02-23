class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        def shiftLeftRight(mat, d):
            new_mat = [[0 for i in range(n)] for j in range(n)]
            for j in range(n):
                for i in range(n):
                    new_mat[i][j] += mat[i][j+d] if 0 <= j+d < n else 0
            return new_mat
        def shiftUpDown(mat, d):
            new_mat = [[0 for i in range(n)] for j in range(n)]
            for j in range(n):
                for i in range(n):
                    new_mat[i][j] += mat[i+d][j] if 0 <= i+d < n else 0
            return new_mat
        def checkOverlay(mat1, mat2):
            size = len(mat1)
            overlays = 0
            for i in range(size):
                for j in range(size):
                    if mat1[i][j] + mat2[i][j] == 2:
                        overlays += 1
            return overlays
        max_overlay = 0
        h_memo = {}
        for h in range(n*-1 + 1,n):
            for v in range(n*-1 + 1, n):
                if h in h_memo:
                    img1_h = h_memo[h]
                else:
                    img1_h = shiftLeftRight(img1, h)
                    h_memo[h] = img1_h
                img1_v_h = shiftUpDown(img1_h, v)
                max_overlay = max(max_overlay, checkOverlay(img1_v_h, img2))
        return max_overlay



        