class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['U' for _ in range(n)] for _ in range(m)]

        for r, c in guards:
            grid[r][c] = "G"
        for r, c in walls:
            grid[r][c] = "W"

        def mark(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] in ("W", "G"):
                    break
                if grid[r][c] == "U":
                    grid[r][c] = "S"
                r += dr
                c += dc

        for r, c in guards:
            mark(r-1, c, -1, 0)
            mark(r+1, c, 1, 0)
            mark(r, c-1, 0, -1)
            mark(r, c+1, 0, 1)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "U":
                    count += 1
        return count