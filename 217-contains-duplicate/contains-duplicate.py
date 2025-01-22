class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        new_nums = set(nums)
        if len(new_nums) != len(nums):
            return True
        else:
            return False
