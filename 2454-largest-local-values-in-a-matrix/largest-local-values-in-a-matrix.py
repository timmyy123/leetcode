class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0 for i in range(n-2)] for j in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                maxLocal[i][j] += max([grid[a][b] for a in range(i, i+3) for b in range(j, j+3)])
        return maxLocal
        