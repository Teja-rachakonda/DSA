class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Store the minimum prefix sum for each remainder (0 to k-1)
        # Initialize with infinity because we want to find the minimum.
        min_offset = [float('inf')] * k
        
        # Base Case: A prefix of length 0 has sum 0 and remainder 0
        min_offset[0] = 0
        
        current_sum = 0
        max_sum = float('-inf')
        
        for i in range(n):
            current_sum += nums[i]
            
            # The current length is (i + 1)
            rem = (i + 1) % k
            
            # If we have a valid previous prefix with the same remainder
            if min_offset[rem] != float('inf'):
                # Calculate the subarray sum ending here
                # subarray_sum = current_prefix - min_prefix_with_same_remainder
                max_sum = max(max_sum, current_sum - min_offset[rem])
            
            # Update the minimum prefix sum for this remainder
            # We want to keep the SMALLEST prefix sum to maximize future results
            min_offset[rem] = min(min_offset[rem], current_sum)
            
        return max_sum