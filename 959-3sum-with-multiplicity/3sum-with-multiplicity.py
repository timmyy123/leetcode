# my
# class Solution:
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         pairs = set()
#         memo = {}
#         for i in range(len(arr)-1):
#             for j in range(i+1, len(arr)):
#                 memo[(i, j)] = arr[i] + arr[j]
#         for (i,j), sum2 in memo.items():
#             for k in range(len(arr)):
#                 if k not in (i, j) and sum2 + arr[k] == target:
#                     pairs.add(tuple(sorted((i,j,k))))
#         return len(pairs)%(10**9 + 7)

# chatgpt
from collections import Counter
from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter()  # Store count of numbers seen so far
        result = 0

        for j in range(len(arr)):  # Iterate over second number (middle)
            # Find number pairs that sum up to (target - arr[j])
            result += count[target - arr[j]]  # Count valid pairs (i, j)
            result %= MOD

            # Update `count` to include numbers before `j`
            for i in range(j):
                count[arr[i] + arr[j]] += 1  # Store sum of (i, j)

        return result
