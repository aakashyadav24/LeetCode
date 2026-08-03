class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        n = len(word)
        x = n % 8
        if n <= 8:
            return n
        elif n <= 16:
            if x == 0:
                return 24
            return 8 + x * 2
        elif n <= 24:
            if x == 0:
                return 48
            return 24 + x * 3
        else:
            return 48 + x * 4