from functools import lru_cache
from math import gcd
from typing import List

MOD = 10**9 + 7

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, g1: int, g2: int) -> int:
            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0

            x = nums[i]

            # Option 1: Skip current element
            ans = dp(i + 1, g1, g2)

            # Option 2: Put it into the first subsequence
            new_g1 = x if g1 == 0 else gcd(g1, x)
            ans += dp(i + 1, new_g1, g2)

            # Option 3: Put it into the second subsequence
            new_g2 = x if g2 == 0 else gcd(g2, x)
            ans += dp(i + 1, g1, new_g2)

            return ans % MOD

        return dp(0, 0, 0)