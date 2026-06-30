class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0] * 3
        left = 0
        ans = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] += 1

            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                ans += len(s) - right
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

        return ans