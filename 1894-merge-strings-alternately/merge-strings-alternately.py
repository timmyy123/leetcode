class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i in range(min(len(word1),len(word2))):
            result+=word1[i]
            result+=word2[i]
        if len(word1) > len(word2):
            result += str(word1[len(word2):])
        if len(word1) < len(word2):
            result += str(word2[len(word1):])
        return result
        