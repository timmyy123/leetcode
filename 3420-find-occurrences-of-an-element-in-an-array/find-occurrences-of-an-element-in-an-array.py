class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrences = list(filter(lambda i: nums[i] == x, range(len(nums)) ))
        return list(map(lambda i: occurrences[i-1] if i <= len(occurrences) else -1, queries))
        