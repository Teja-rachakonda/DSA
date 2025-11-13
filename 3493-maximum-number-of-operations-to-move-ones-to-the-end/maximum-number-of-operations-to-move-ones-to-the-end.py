class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == "1":
                ones += 1
                i += 1
            else:
                ans += ones
                while i < n and s[i] == "0":
                    i += 1
        return ans