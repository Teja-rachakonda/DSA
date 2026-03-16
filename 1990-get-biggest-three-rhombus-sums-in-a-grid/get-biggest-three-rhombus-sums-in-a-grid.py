from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        # A set automatically handles the "distinct" values requirement
        distinct_sums = set()
        
        # Treat every cell (i, j) as the TOP vertex of a rhombus
        for i in range(m):
            for j in range(n):
                
                # Base Case: Area 0 rhombus (just the cell itself)
                distinct_sums.add(grid[i][j])
                
                # Expand the rhombus size (L is the length of the edge)
                L = 1
                
                # Keep expanding as long as the bottom, left, and right vertices are in bounds
                while i + 2 * L < m and j - L >= 0 and j + L < n:
                    current_sum = 0
                    r, c = i, j
                    
                    # 1. Walk Down-Right
                    for _ in range(L):
                        current_sum += grid[r][c]
                        r += 1
                        c += 1
                        
                    # 2. Walk Down-Left
                    for _ in range(L):
                        current_sum += grid[r][c]
                        r += 1
                        c -= 1
                        
                    # 3. Walk Up-Left
                    for _ in range(L):
                        current_sum += grid[r][c]
                        r -= 1
                        c -= 1
                        
                    # 4. Walk Up-Right
                    for _ in range(L):
                        current_sum += grid[r][c]
                        r -= 1
                        c += 1
                        
                    distinct_sums.add(current_sum)
                    L += 1  # Try a bigger rhombus
                    
        # Sort the distinct sums in descending order and return up to the top 3
        return sorted(list(distinct_sums), reverse=True)[:3]