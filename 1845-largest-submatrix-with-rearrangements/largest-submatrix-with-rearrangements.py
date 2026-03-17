from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        
        # Step 1: Build the heights (histograms) vertically
        for i in range(m):
            for j in range(n):
                # If it's a 1 and not the first row, accumulate the height from above
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
                    
            # Step 2: Sort the heights of the current row in descending order
            # We sort a copy of the row so we don't mess up the actual matrix 
            # for the subsequent rows that depend on it!
            sorted_heights = sorted(matrix[i], reverse=True)
            
            # Step 3: Calculate the maximum area ending at this row
            for j in range(n):
                # If the height is 0, we can't form a rectangle anyway
                if sorted_heights[j] == 0:
                    break
                    
                # Area = height * width
                current_area = sorted_heights[j] * (j + 1)
                max_area = max(max_area, current_area)
                
        return max_area