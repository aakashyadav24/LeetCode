class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        i = 1
        n = len(nums)
        for num in nums:
            if  n % i == 0:
                add = num * num
                ans += add
            i += 1
        return ans