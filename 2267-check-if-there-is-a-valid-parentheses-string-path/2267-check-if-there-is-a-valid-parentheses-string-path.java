class Solution {
    public boolean hasValidPath(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int len = m + n - 1;

        // A valid parentheses string must have even length.
        if (len % 2 != 0) {
            return false;
        }

        // dp[j][balance] = whether balance is possible
        // at the cell currently represented by column j.
        boolean[][] dp = new boolean[n][len + 1];

        // At (0, 0), process the first character.
        if (grid[0][0] == ')') {
            return false;
        }

        dp[0][1] = true;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (i == 0 && j == 0) {
                    continue;
                }

                boolean[] current = new boolean[len + 1];

                int change = grid[i][j] == '(' ? 1 : -1;

                for (int balance = 0; balance <= len; balance++) {

                    // From above.
                    if (i > 0 && dp[j][balance]) {
                        int newBalance = balance + change;

                        if (newBalance >= 0 && newBalance <= len) {
                            current[newBalance] = true;
                        }
                    }

                    // From left.
                    if (j > 0 && dp[j - 1][balance]) {
                        int newBalance = balance + change;

                        if (newBalance >= 0 && newBalance <= len) {
                            current[newBalance] = true;
                        }
                    }
                }

                dp[j] = current;
            }
        }

        return dp[n - 1][0];
    }
}
