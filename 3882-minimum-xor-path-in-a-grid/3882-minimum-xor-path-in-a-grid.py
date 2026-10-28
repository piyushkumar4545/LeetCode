class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 << grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                prev = 0
                if i > 0:
                    prev |= dp[i - 1][j]
                if j > 0:
                    prev |= dp[i][j - 1]

                val = grid[i][j]
                mask = 0

                for x in range(1024):
                    if prev & (1 << x):
                        mask |= 1 << (x ^ val)

                dp[i][j] = mask

        bits = dp[m - 1][n - 1]
        return (bits & -bits).bit_length() - 1