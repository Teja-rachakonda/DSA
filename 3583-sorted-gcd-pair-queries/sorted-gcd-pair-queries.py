from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        # Frequency of each value
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = how many numbers are divisible by d
        cnt = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            for multiple in range(d, max_val + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs whose gcd is exactly d
        exact = [0] * (max_val + 1)

        for d in range(max_val, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2

            multiple = 2 * d
            while multiple <= max_val:
                pairs -= exact[multiple]
                multiple += d

            exact[d] = pairs

        # Prefix counts of gcd values
        prefix = []
        values = []
        total = 0

        for g in range(1, max_val + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans