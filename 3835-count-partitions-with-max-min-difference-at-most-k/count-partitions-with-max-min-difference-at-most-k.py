from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # dp[i] = number of ways to partition the prefix of length i
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to partition an empty prefix
        
        # Prefix sum of dp array to calculate range sums in O(1)
        # dp_presum[i] stores sum(dp[0]...dp[i])
        dp_presum = [0] * (n + 1)
        dp_presum[0] = 1
        
        # Monotonic deques to maintain max and min in the current window [left, i]
        max_d = deque() # Stores indices, values decreasing
        min_d = deque() # Stores indices, values increasing
        
        left = 0
        
        for i in range(n):
            # 1. Update Max Deque
            while max_d and nums[max_d[-1]] <= nums[i]:
                max_d.pop()
            max_d.append(i)
            
            # 2. Update Min Deque
            while min_d and nums[min_d[-1]] >= nums[i]:
                min_d.pop()
            min_d.append(i)
            
            # 3. Shrink window from the left if validity is violated
            while nums[max_d[0]] - nums[min_d[0]] > k:
                # Increment left pointer
                left += 1
                # Remove indices from deques if they fall out of the new window
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()
            
            # 4. Calculate dp[i+1]
            # Valid start indices for the last segment are in range [left, i].
            # We need sum(dp[j]) for left <= j <= i.
            # Using prefix sums: sum = dp_presum[i] - dp_presum[left-1]
            
            current_sum = dp_presum[i]
            if left > 0:
                current_sum -= dp_presum[left - 1]
            
            dp[i+1] = current_sum % MOD
            
            # Update prefix sum for the next iteration
            dp_presum[i+1] = (dp_presum[i] + dp[i+1]) % MOD
            
        return dp[n]