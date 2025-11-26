class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        start_val = grid[0][0]
        dp[0][0][start_val % k] = 1

        for i in range(m):
            for j in range(n):
                cell_val = grid[i][j]

                for rem in range(k):
                    prev_rem = (rem - cell_val) % k
                

                    if i > 0:
                        dp[i][j][rem] = (dp[i][j][rem] + dp[i - 1][j][prev_rem]) % MOD
                    if j > 0:
                        dp[i][j][rem] = (dp[i][j][rem] + dp[i][j - 1][prev_rem]) % MOD
        return dp[m-1][n-1][0]