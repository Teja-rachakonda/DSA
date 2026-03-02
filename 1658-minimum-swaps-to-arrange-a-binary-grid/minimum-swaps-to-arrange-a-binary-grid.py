from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        
        
        for row in grid:
            count = 0
    
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
            
        swaps = 0
        
    
        for i in range(n):
            target = n - 1 - i
            found_idx = -1
            
         
            for j in range(i, n):
                if zeros[j] >= target:
                    found_idx = j
                    break
          
            if found_idx == -1:
                return -1

            swaps += (found_idx - i)
            
    
            val = zeros.pop(found_idx)
            zeros.insert(i, val)
            
        return swaps