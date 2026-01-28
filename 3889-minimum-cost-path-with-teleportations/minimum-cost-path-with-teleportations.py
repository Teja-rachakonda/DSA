from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] stores the min cost to reach (m-1, n-1) starting from (i, j)
        # Initialize with infinity
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Base case: Cost at destination is 0 (cost is incurred upon entering a cell)
        dp[m-1][n-1] = 0
        
        # Helper to perform the backward walk (Right/Down moves)
        # This propagates the cost from the destination backwards
        def backward_walk():
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        continue
                    
                    current_min = dp[i][j]
                    
                    # Try moving Down
                    if i + 1 < m:
                        current_min = min(current_min, dp[i+1][j] + grid[i+1][j])
                    
                    # Try moving Right
                    if j + 1 < n:
                        current_min = min(current_min, dp[i][j+1] + grid[i][j+1])
                        
                    dp[i][j] = current_min

        # 1. Initial pass for k=0 (Pure walking)
        backward_walk()
        
        # Prepare cells list for teleport logic: (value, row, col)
        # Sorting allows us to efficiently find min(dp[dest]) where grid[dest] <= grid[src]
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort(key=lambda x: x[0])
        
        # 2. Iterate k times to add teleports
        for _ in range(k):
            # --- Teleport Pass ---
            # We process cells in batches of equal grid value.
            # All cells in a batch (and previous batches) are valid destinations 
            # for a teleport starting from any cell in the current batch.
            
            global_min = float('inf')
            idx = 0
            num_cells = len(cells)
            
            while idx < num_cells:
                # Identify the range [idx, end) having the same grid value
                end = idx
                while end < num_cells and cells[end][0] == cells[idx][0]:
                    end += 1
                
                # 1. Find the min cost among the current batch
                batch_min = float('inf')
                for i in range(idx, end):
                    r, c = cells[i][1], cells[i][2]
                    batch_min = min(batch_min, dp[r][c])
                
                # 2. The effective min cost available to this batch is min(global_min, batch_min)
                # global_min covers all cells with strictly smaller values.
                # batch_min covers all cells with equal values.
                combined_min = min(global_min, batch_min)
                
                # 3. Update the global min for future batches (larger values)
                global_min = combined_min
                
                # 4. Apply teleport: any cell in this batch can jump to the best spot found so far
                for i in range(idx, end):
                    r, c = cells[i][1], cells[i][2]
                    dp[r][c] = min(dp[r][c], combined_min)
                
                # Move to next batch
                idx = end
                
            # --- Walk Pass ---
            # After teleporting, we might need to walk to the finish.
            backward_walk()
            
        return dp[0][0]