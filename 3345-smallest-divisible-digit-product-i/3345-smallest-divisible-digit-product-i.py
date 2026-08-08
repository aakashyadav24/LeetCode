class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(n, t):
            prod = 1
            while n != 0:
                digit = n % 10
                prod = prod * digit
                n = n // 10
            if prod % t == 0:
                return True
            else:
                return False
        for i in range(11):
            ans = check(n+i, t)
            if ans:
                return n + i
            else:
                continue
            