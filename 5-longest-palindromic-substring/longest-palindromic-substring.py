# my solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        for length in range(1, len(s)+1):  # Length should go up to len(s)
            for i in range(len(s) - length + 1):  # Make sure the slice is within bounds
                substring = s[i:i+length]
                if substring == substring[::-1]:
                    # Update result if the new palindrome is longer
                    if len(substring) > len(result):
                        result = substring
        return result

# chatgpt
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand_from_center(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left+1:right]

#         result = ""
#         for i in range(len(s)):
#             # Odd length palindromes
#             odd_palindrome = expand_from_center(i, i)
#             # Even length palindromes
#             even_palindrome = expand_from_center(i, i+1)
            
#             # Choose the longest palindrome
#             result = max(result, odd_palindrome, even_palindrome, key=len)
        
#         return result


            


        