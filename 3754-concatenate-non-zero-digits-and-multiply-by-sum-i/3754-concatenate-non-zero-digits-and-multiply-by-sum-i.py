class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sm = 0
        x = ''
        nums = str(n)
        for num in nums:
            if num != '0':
                x += num
                sm += int(num)
        if x == '':
            return 0
        return int(x) * sm
