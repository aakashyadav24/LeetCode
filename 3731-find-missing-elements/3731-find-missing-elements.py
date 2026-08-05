class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        start = nums[0]
        end = nums[-1]
        ans = []
        for i in range(start + 1, end):
            if i not in nums:
                ans.append(i)
        return ans