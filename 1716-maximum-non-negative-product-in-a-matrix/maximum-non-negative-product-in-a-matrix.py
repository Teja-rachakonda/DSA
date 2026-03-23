from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
    
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
       
        for j in range(1, n):
            max_dp[0][j] = max_dp[0][j-1] * grid[0][j]
            min_dp[0][j] = min_dp[0][j-1] * grid[0][j]
            
       
        for i in range(1, m):
            max_dp[i][0] = max_dp[i-1][0] * grid[i][0]
            min_dp[i][0] = min_dp[i-1][0] * grid[i][0]
            

        for i in range(1, m):
            for j in range(1, n):
                
          
                up_max = max_dp[i-1][j] * grid[i][j]
                up_min = min_dp[i-1][j] * grid[i][j]
                left_max = max_dp[i][j-1] * grid[i][j]
                left_min = min_dp[i][j-1] * grid[i][j]
                
              
                max_dp[i][j] = max(up_max, up_min, left_max, left_min)
                min_dp[i][j] = min(up_max, up_min, left_max, left_min)
                
       
        ans = max_dp[-1][-1]
        
   
        return ans % MOD if ans >= 0 else -1