
import java.util.*;

class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.length;

        // Prefix sums
        long[] pref = new long[n + 1];

        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }

        // Find next strictly greater element
        int[] next = new int[n];
        Arrays.fill(next, n);

        Deque<Integer> st = new ArrayDeque<>();

        for (int i = n - 1; i >= 0; i--) {
            while (!st.isEmpty() && nums[st.peek()] <= nums[i]) {
                st.pop();
            }

            if (!st.isEmpty()) {
                next[i] = st.peek();
            }

            st.push(i);
        }

        // Binary lifting
        int LOG = 1;
        while ((1 << LOG) <= n) {
            LOG++;
        }

        int[][] up = new int[LOG][n];
        long[][] sum = new long[LOG][n];

        // Base level
        for (int i = 0; i < n; i++) {
            up[0][i] = next[i];

            int end = next[i];

            sum[0][i] =
                (long) nums[i] * (end - i)
                - (pref[end] - pref[i]);
        }

        // Build lifting tables
        for (int p = 1; p < LOG; p++) {
            for (int i = 0; i < n; i++) {
                int mid = up[p - 1][i];

                if (mid < n) {
                    up[p][i] = up[p - 1][mid];

                    sum[p][i] =
                        sum[p - 1][i] + sum[p - 1][mid];
                } else {
                    up[p][i] = n;
                    sum[p][i] = sum[p - 1][i];
                }
            }
        }

        // Calculate operations required for [l, r]
        // using binary lifting
        long[] dummy = new long[1];

        long ans = 0;

        for (int r = 0; r < n; r++) {
            int lo = 0;
            int hi = r;

            // Find smallest valid left boundary
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;

                long cost = 0;
                int cur = mid;

                for (int p = LOG - 1; p >= 0; p--) {
                    if (up[p][cur] <= r) {
                        cost += sum[p][cur];
                        cur = up[p][cur];
                    }
                }

                // Remaining partial maximum segment
                cost += (long) nums[cur] * (r - cur + 1)
                      - (pref[r + 1] - pref[cur]);

                if (cost <= k) {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }

            ans += r - lo + 1;
        }

        return ans;
    }
}
