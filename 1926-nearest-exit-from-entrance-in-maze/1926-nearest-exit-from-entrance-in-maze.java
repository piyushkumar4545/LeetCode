
import java.util.*;

class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {

        int m = maze.length;
        int n = maze[0].length;

        Queue<int[]> q = new LinkedList<>();

        q.add(new int[]{entrance[0], entrance[1], 0});

        // Mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+';

        int[][] directions = {
            {-1, 0},  // Up
            {1, 0},   // Down
            {0, -1},  // Left
            {0, 1}    // Right
        };

        while (!q.isEmpty()) {

            int[] curr = q.poll();

            int r = curr[0];
            int c = curr[1];
            int steps = curr[2];

            for (int[] d : directions) {

                int nr = r + d[0];
                int nc = c + d[1];

                // Check boundaries
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }

                // Skip walls and visited cells
                if (maze[nr][nc] == '+') {
                    continue;
                }

                // Check if current cell is an exit
                if (nr == 0 || nr == m - 1 ||
                    nc == 0 || nc == n - 1) {
                    return steps + 1;
                }

                // Mark visited
                maze[nr][nc] = '+';

                q.add(new int[]{nr, nc, steps + 1});
            }
        }

        return -1;
    }
}
