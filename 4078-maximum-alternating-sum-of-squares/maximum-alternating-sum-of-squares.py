
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums])

        n = len(squares)
        positive = squares[(n + 1) // 2:]
        negative = squares[:n // 2]

        return sum(squares) - 2 * sum(negative)
