class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        t0, t1, t2 = 0, 1, 1
        tn = t0 + t1 + t2
        if n == 3:
            return tn
        for i in range(4, n+1):
            t1, t2, tn = t2, tn, (t1+t2+tn)
        return tn
        