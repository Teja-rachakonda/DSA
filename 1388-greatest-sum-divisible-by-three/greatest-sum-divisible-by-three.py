class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        if total_sum % 3 == 0:
            return total_sum
        
        rem_1 = []
        rem_2 = []

        for n in nums:
            if n % 3 == 1:
                rem_1.append(n)
            elif n % 3 == 2:
                rem_2.append(n)
        
        rem_1.sort()
        rem_2.sort()

        remainder = total_sum % 3

        to_remove = float("inf")

        if remainder == 1:
            if len(rem_1) >=1:
                to_remove = min(to_remove, rem_1[0])
            if len(rem_2) >= 2:
                to_remove = min(to_remove, rem_2[0] + rem_2[1])
        
        elif remainder == 2:
            if len(rem_2) >= 1:
                to_remove = min(to_remove, rem_2[0])
            if len(rem_1) >= 2:
                to_remove = min(to_remove, rem_1[0] + rem_1[1])
        return total_sum - to_remove
