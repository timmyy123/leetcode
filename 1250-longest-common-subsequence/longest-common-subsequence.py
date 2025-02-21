class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(i, j):
            if j >= len(text2) or i >= len(text1):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            k = text1[i:].find(text2[j]) + i
            memo[(i, j)] = max(dp(k+1, j+1)+1, dp(i, j+1)) if k - i != -1 else dp(i, j+1)
            return memo[(i, j)]
        return dp(0,0)