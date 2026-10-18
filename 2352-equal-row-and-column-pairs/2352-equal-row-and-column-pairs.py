from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # Count occurrences of each row
        row_count = Counter(tuple(row) for row in grid)

        ans = 0

        # Build each column and count matching rows
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            ans += row_count[col]

        return ans