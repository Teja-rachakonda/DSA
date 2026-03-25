from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Collapse the 2D grid into 1D arrays representing row and column totals
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(col) for col in zip(*grid)]
        
        total_sum = sum(row_sums)
        
        # If the total sum is odd, we can never split it equally
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # --- Check for a valid horizontal cut ---
        current_sum = 0
        # Loop up to m - 1 to guarantee the bottom section isn't empty
        for i in range(m - 1):
            current_sum += row_sums[i]
            if current_sum == target:
                return True
                
        # --- Check for a valid vertical cut ---
        current_sum = 0
        # Loop up to n - 1 to guarantee the right section isn't empty
        for j in range(n - 1):
            current_sum += col_sums[j]
            if current_sum == target:
                return True
                
        # If neither a horizontal nor vertical cut works
        return False