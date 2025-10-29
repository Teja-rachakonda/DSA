class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(32):
            if (1 << i) - 1 >= n:
                return (1 << i) - 1