class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        z = 0
        for i in nums:
            r = i - 1
            t = i + 1
            if r % 3 == 0:
                z += 1
            elif t % 3 == 0:
                z += 1
        return z
