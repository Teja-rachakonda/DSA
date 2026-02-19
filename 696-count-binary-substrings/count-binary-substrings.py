class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_len = 0
        curr_len = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_len += 1
            else:
                ans += min(prev_len, curr_len)
                prev_len = curr_len
                curr_len = 1
        ans += min(prev_len, curr_len)
        return ans