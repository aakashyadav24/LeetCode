class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = max(nums)
        if maximum < 0:
            return maximum
        max_so_far = 0
        max_ending_here = 0

        for num in nums:
            max_ending_here += num
            max_ending_here = max(max_ending_here, 0)

            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far