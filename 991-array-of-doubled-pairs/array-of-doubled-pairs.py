from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        if len(arr) % 2 != 0:
            return False
        positive_group = list(filter(lambda x: x>=0, arr))
        if len(positive_group) % 2 != 0:
            return False
        # zero_group = list(filter(lambda x: x==0, arr))
        # if len(zero_group)%2 != 0:
        #     return False
        negative_group = map(lambda x: abs(x),list(filter(lambda x: x<0, arr)))
        def validate(group):
            count = Counter(group)
            for num in sorted(count.keys()):
                if count[num] > count[num * 2]:  # If we have more num than 2*num, it's impossible
                    return False
                count[num * 2] -= count[num]  # Pair them properly
                count[num] = 0  # Mark as processed
            for num in count.values():
                if num != 0:
                    return False
            return True
        return validate(positive_group) and validate(negative_group)
                    

        