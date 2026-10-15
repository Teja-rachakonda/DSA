class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                dict = {}
                for t in range(i, j + 1):

                    if nums[t] not in dict:
                        dict[nums[t]] = 1
                    else:
                        dict[nums[t]] += 1
                ans += len(dict) * len(dict)
        return ans