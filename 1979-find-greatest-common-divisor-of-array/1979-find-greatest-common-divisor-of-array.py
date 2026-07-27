class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        mn , mx = nums[0], nums[-1]
        print(mn, mx)
        for i in range(mx, -1, -1):
            if mx % i == 0 and mn % i == 0:
                return i
        return 1