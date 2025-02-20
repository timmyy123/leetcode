class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        acc_dic = {0:0}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            acc_dic[i+1] = cur_sum
        for j in range(len(nums)):
            if acc_dic[j] == cur_sum - acc_dic[j+1]:
                return j
        return -1
        