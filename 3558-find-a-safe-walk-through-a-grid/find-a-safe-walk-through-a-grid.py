from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # Health after standing on the starting cell
        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

        # best[r][c] = maximum remaining health seen at this cell
        best = [[-1] * n for _ in range(m)]
        best[0][0] = start_health

        q = deque([(0, 0, start_health)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, curr_health = q.popleft()

            # Reached destination
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    new_health = curr_health - grid[nr][nc]

                    if new_health <= 0:
                        continue

                    # Visit only if this path is better
                    if new_health > best[nr][nc]:
                        best[nr][nc] = new_health
                        q.append((nr, nc, new_health))

        return False