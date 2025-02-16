class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 0 and len(s.strip()) == 0:
            return 1     
        if len(s.strip()) == 1:
            return 1
        length = 0
        for subIndex in range(len(s) -1):
            chars = set()
            string_compare = ''
            for char in s[subIndex:]:
                if char not in chars:
                    string_compare+=char
                    chars.add(char)
                else:
                    break
                if len(string_compare) > length:
                    length = len(string_compare)
        return length
        