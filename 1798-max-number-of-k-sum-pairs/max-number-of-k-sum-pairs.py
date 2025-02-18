class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i, j = 0, len(nums)-1
        if i == j:
            return 1 if nums[i] == k else 0
        operations = 0
        nums.sort()
        while i < j:
            if nums[i] + nums[j] == k:
                operations += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return operations

        