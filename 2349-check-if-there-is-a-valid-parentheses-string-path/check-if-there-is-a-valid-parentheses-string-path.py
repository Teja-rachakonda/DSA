class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # dp[i][j] stores all possible balances
        # when reaching cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # The first character must be '('
        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # Collect possible balances from
                # the cell above and the cell to the left
                previous_balances = set()

                if i > 0:
                    previous_balances.update(dp[i - 1][j])

                if j > 0:
                    previous_balances.update(dp[i][j - 1])

                # Number of cells remaining after this cell
                remaining = (m - 1 - i) + (n - 1 - j)

                for balance in previous_balances:

                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Invalid prefix
                    if new_balance < 0:
                        continue

                    # Not enough remaining cells to close
                    # all currently open parentheses
                    if new_balance > remaining:
                        continue

                    dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]