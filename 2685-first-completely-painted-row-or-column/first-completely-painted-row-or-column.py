class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        num_to_position = {}
    
        for i in range(m):
            for j in range(n):
                num_to_position[mat[i][j]] = (i, j)
        
        # Initialize row and column counts
        row_count = [0] * m
        col_count = [0] * n
        
        # Process each number in arr
        for idx, num in enumerate(arr):
            row, col = num_to_position[num]
            row_count[row] += 1
            col_count[col] += 1
        
        # Check if a row or column is fully painted
            if row_count[row] == n or col_count[col] == m:
                return idx
    
        return -1 