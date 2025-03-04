class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds_index = []
        for i in range(len(nums)):
            if nums[i] %2 == 1:
                odds_index.append(i)
        if len(odds_index) < k:
            return 0
        result = 0
        print(odds_index)
        for i in range(len(odds_index)-k+1):
            print(odds_index[i]-(odds_index[i-1] if i-1 >= 0 else 0))
            print((odds_index[i+k] if i+k <= len(odds_index) -1 else len(nums) -1) - odds_index[i+k-1])
            result += (odds_index[i]-(odds_index[i-1] if i-1 >= 0 else -1))*((odds_index[i+k] if i+k <= len(odds_index) -1 else len(nums)) - odds_index[i+k-1])
        return result

        