# my own
import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        digits = math.floor(math.log(x,10))+1
        for i in range(1, (digits//2)+1):
            if x%(10**i)//(10**(i-1)) != x%(10**(digits-i+1))//(10**(digits-i)):
                return False
        return True

# chatgpt
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # Negative numbers are not palindromes
#         # Numbers ending in 0 are not palindromes unless the number is 0
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
        
#         reversed_half = 0
#         while x > reversed_half:
#             reversed_half = reversed_half * 10 + x % 10
#             x //= 10
        
#         # When the length is an odd number, get rid of the middle digit by reversed_half//10
#         return x == reversed_half or x == reversed_half // 10

        