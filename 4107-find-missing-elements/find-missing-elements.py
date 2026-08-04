class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 1):
            for x in range(nums[i] + 1, nums[i + 1]):
                ans.append(x)

        return ans