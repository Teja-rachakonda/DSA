class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                result.append(nums[i])
        return result