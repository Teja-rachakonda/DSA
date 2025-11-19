class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if original == nums[i]:
                z = nums[i] * 2
                original = z
        return original