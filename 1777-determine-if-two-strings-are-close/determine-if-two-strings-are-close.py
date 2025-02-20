class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        def count_char(word):
            char_count = {}
            for i in range(len(word)):
                char_count[word[i]] = (char_count[word[i]] + 1) if word[i] in char_count.keys() else 1
            return char_count
        dic1 = count_char(word1)
        dic2 = count_char(word2)
        print(dic1, dic2)
        chars1 = list(dic1.keys())
        chars2 = list(dic2.keys())
        counts1 = list(dic1.values())
        counts2 = list(dic2.values())
        print(chars1, chars2, counts1, counts2)
        chars1.sort()
        chars2.sort()
        counts1.sort()
        counts2.sort()
        print(chars1, chars2, counts1, counts2)
        if len(chars1) != len(chars2):
            return False
        for i in range(len(chars1)):
            if chars1[i] != chars2[i]:
                return False
        for j in range(len(counts1)):
            if counts1[j] != counts2[j]:
                return False
        return True

        