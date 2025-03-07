class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                x, y = j+1, len(nums) -1
                while x<y:
                    if nums[i] + nums[j] + nums[x] + nums[y] == target:
                        result.append([nums[i], nums[j], nums[x], nums[y]])
                        while x<y and nums[x+1] == nums[x]:
                            x += 1
                        while y>x and nums[y-1] == nums[y]:
                            y -= 1
                        x+=1
                        y-=1
                    elif nums[i] + nums[j] + nums[x] + nums[y] < target:
                        x+=1
                    else:
                        y-=1
        return result
                    


        