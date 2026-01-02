class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for key, value in dict.items():
            if value > 1:
                return key