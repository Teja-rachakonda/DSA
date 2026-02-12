class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            counts = {}
            max_freq = 0
            for j in range(i, n):
                char = s[j]
                counts[char] = counts.get(char, 0) + 1
                max_freq = max(max_freq, counts[char])

                current_len = j - i + 1
                if max_freq * len(counts) == current_len:
                    max_len = max(max_len, current_len)
        return max_len