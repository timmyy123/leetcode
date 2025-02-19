class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_li = {'a', 'e', 'i', 'o', 'u'}
        sum_dic = {}
        cur_sum = 0
        for i in range(len(s)):
            if s[i] in vowels_li:
                cur_sum += 1
            sum_dic[i] = cur_sum
        max_vowels = sum_dic[k-1]
        for j in range(1,len(s)-k+1):
            max_vowels = max(max_vowels, (sum_dic[j+k-1] - sum_dic[j-1]))
        return max_vowels


        