class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        t = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                t.append(i)
        return t