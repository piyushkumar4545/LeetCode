
class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {

        Map<String, Map<String, Double>> graph = new HashMap<>();

        // Build graph
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0);
            String b = equations.get(i).get(1);

            double val = values[i];

            graph.putIfAbsent(a, new HashMap<>());
            graph.putIfAbsent(b, new HashMap<>());

            graph.get(a).put(b, val);
            graph.get(b).put(a, 1.0 / val);
        }

        double[] ans = new double[queries.size()];

        // Process queries
        for (int i = 0; i < queries.size(); i++) {
            String src = queries.get(i).get(0);
            String dest = queries.get(i).get(1);

            if (!graph.containsKey(src) || !graph.containsKey(dest)) {
                ans[i] = -1.0;
            } else if (src.equals(dest)) {
                ans[i] = 1.0;
            } else {
                Set<String> visited = new HashSet<>();
                ans[i] = dfs(graph, src, dest, visited);
            }
        }

        return ans;
    }

    private double dfs(Map<String, Map<String, Double>> graph,
                       String src, String dest,
                       Set<String> visited) {

        if (src.equals(dest)) {
            return 1.0;
        }

        visited.add(src);

        for (Map.Entry<String, Double> entry : graph.get(src).entrySet()) {
            String next = entry.getKey();
            double weight = entry.getValue();

            if (!visited.contains(next)) {
                double result = dfs(graph, next, dest, visited);

                if (result != -1.0) {
                    return weight * result;
                }
            }
        }

        return -1.0;
    }
}
