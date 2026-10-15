class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        ans = []
        nines = sum // 9 
        for i in range(nines):
            ans.append("9")
        remainder = sum % 9
        if remainder > 0:
            ans.append(str(remainder))
        zeroes = num - len(ans)
        ans.append('0' * zeroes)
        return "".join(ans)
