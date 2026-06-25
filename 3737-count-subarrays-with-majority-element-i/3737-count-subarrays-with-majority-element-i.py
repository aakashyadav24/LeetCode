class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        # prefix[i] = number of times target appears in nums[:i]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if nums[i] == target else 0)

        # check subarrays using prefix counts
        for i in range(n):
            for j in range(i, n):
                count_target = prefix[j+1] - prefix[i]
                length = j - i + 1
                if 2 * count_target > length:
                    ans += 1
        return ans
