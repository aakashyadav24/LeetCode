class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                sub_arr = nums[i: j+1]
                unique = set(sub_arr)
                ans += len(unique) ** 2
        return ans        