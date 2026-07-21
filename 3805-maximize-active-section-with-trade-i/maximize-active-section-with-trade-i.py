class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        # Augment the string with '1' at both ends
        t = '1' + s + '1'

        # Run-Length Encoding: (character, length)
        blocks = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j

        max_gain = 0

        # Find every 1-block surrounded by 0-blocks
        for i in range(1, len(blocks) - 1):
            if (
                blocks[i][0] == '1'
                and blocks[i - 1][0] == '0'
                and blocks[i + 1][0] == '0'
            ):
                gain = blocks[i - 1][1] + blocks[i + 1][1]
                max_gain = max(max_gain, gain)

        return ones + max_gain