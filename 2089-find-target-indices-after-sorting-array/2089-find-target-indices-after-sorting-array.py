class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        count = 0
        idx = 0
        for num in nums:
            if num < target:
                idx += 1
            if num == target:
                count += 1
        for i in range(count):
            ans.append(idx + i)
        return ans

        