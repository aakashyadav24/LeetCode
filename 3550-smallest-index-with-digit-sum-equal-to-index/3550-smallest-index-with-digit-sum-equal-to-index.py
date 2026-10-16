class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = str(nums[i])
            sumd = 0
            for digit in num:
                sumd += int(digit)
            if sumd == i:
                return i
        return -1

        