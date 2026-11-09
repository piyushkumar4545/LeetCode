
import java.util.*;

class Solution {
    public int minReorder(int n, int[][] connections) {
        List<int[]>[] graph = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] edge : connections) {
            int a = edge[0];
            int b = edge[1];

            // Original direction a -> b
            graph[a].add(new int[]{b, 1});

            // Reverse direction b -> a
            graph[b].add(new int[]{a, 0});
        }

        return dfs(0, -1, graph);
    }

    private int dfs(int node, int parent, List<int[]>[] graph) {
        int changes = 0;

        for (int[] edge : graph[node]) {
            int neighbor = edge[0];
            int cost = edge[1];

            if (neighbor == parent) {
                continue;
            }

            changes += cost;
            changes += dfs(neighbor, node, graph);
        }

        return changes;
    }
}
