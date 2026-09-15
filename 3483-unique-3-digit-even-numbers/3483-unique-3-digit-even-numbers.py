class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:  # distinct indices
                        if digits[i] != 0 and digits[k] % 2 == 0:  # valid number
                            num = digits[i] * 100 + digits[j] * 10 + digits[k]
                            nums.add(num)
        return len(nums)
