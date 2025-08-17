class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result.append(0)
        if n == 1:
            return result
        for i in range(1, (n//2)+1):
            result.append(i)
            result.append(-i)
        return result