class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        for sum in range(m+n-1):
            if sum % 2 == 0:
                for j in range(max(0, sum-m+1), min(sum+1, n)):
                    result.append(mat[sum-j][j])
            if sum % 2 == 1:
                for i in range(max(0, sum-n+1), min(sum+1, m)):
                    result.append(mat[i][sum-i])
        return result
        