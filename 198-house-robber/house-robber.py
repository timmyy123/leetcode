# mine
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return max(nums)
#         return max((nums[0] + (self.rob(nums[2:]) if len(nums) > 2 else 0)), (nums[1] + (self.rob(nums[3:]) if len(nums)>3 else 0)))

# from typing import List
# chatgpt
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0
        for num in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + num)
            prev2 = temp
        
        return prev1
