
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        total = sum(nums)

        return total - minimum * len(nums)
