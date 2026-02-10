from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Iterate over all possible start points
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            # Expand the subarray to the right
            for j in range(i, n):
                val = nums[j]
                
                # Add current number to the appropriate set
                if val % 2 == 0:
                    distinct_evens.add(val)
                else:
                    distinct_odds.add(val)
                
                # Check if the counts of distinct elements match
                if len(distinct_evens) == len(distinct_odds):
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len