class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_len = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    cur_len += 1
                else:
                    max_len = max(cur_len, max_len)
                    cur_len = 1
        return max(max_len, cur_len)