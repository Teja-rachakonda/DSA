class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        # Convert 2D grid to 1D list
        arr = []
        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total

        # Rotate the array
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D grid
        ans = []
        idx = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[idx])
                idx += 1
            ans.append(row)

        return ans