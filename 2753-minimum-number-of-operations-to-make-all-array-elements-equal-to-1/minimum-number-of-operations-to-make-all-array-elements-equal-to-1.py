from math import gcd
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        g = nums[0]
        for num in nums[1:]:
            g = gcd(g, num)
        if g > 1:
            return -1

        count_ones = nums.count(1)
        if count_ones > 0:
            return n - count_ones

        min_len = float("inf")
        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        return n + min_len - 2