class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations =0
        while True:
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return operations
            
            min_sum = float("inf")
            min_index = -1

            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_index = i

            new_nums = []
            for i in range(min_index):
                new_nums.append(nums[i]) 
            new_nums.append(min_sum)

            for i in range(min_index + 2, len(nums)):
                new_nums.append(nums[i])

            nums = new_nums
            operations += 1