class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n:
            digit = n % 10
            digits.append(digit)
            n = n // 10
        digits.sort()
        print(digits)
        return int(digits[-1] * digits[-2])