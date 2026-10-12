class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        t = 0
        j = len(nums)
        
        for i in range(1, j + 1):
            if j % i == 0:
                t += nums[i - 1] * nums[i - 1]
        return t