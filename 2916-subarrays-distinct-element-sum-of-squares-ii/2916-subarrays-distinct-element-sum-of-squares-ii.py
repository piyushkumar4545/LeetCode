class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays (size 4 * n is sufficient)
        # s1 stores the sum of elements
        # s2 stores the sum of squares of elements
        # lazy stores the pending additions
        s1 = [0] * (4 * n)
        s2 = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_down(node, l, r):
            if lazy[node] == 0:
                return
            
            add = lazy[node]
            mid = (l + r) // 2
            left_len = mid - l + 1
            right_len = r - mid
            
            # Update left child
            s2[2 * node] = (s2[2 * node] + 2 * add * s1[2 * node] + left_len * add * add) % MOD
            s1[2 * node] = (s1[2 * node] + left_len * add) % MOD
            lazy[2 * node] += add
            
            # Update right child
            s2[2 * node + 1] = (s2[2 * node + 1] + 2 * add * s1[2 * node + 1] + right_len * add * add) % MOD
            s1[2 * node + 1] = (s1[2 * node + 1] + right_len * add) % MOD
            lazy[2 * node + 1] += add
            
            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                length = r - l + 1
                s2[node] = (s2[node] + 2 * val * s1[node] + length * val * val) % MOD
                s1[node] = (s1[node] + length * val) % MOD
                lazy[node] += val
                return
            
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
                
            s1[node] = (s1[2 * node] + s1[2 * node + 1]) % MOD
            s2[node] = (s2[2 * node] + s2[2 * node + 1]) % MOD

        total_sum = 0
        last_seen = {}
        
        for j in range(n):
            # Find the last time nums[j] appeared
            last_idx = last_seen.get(nums[j], -1)
            
            # Increment the distinct count by 1 for all subarrays starting from last_idx + 1 to j
            update(1, 0, n - 1, last_idx + 1, j, 1)
            
            # Add the sum of squares of all subarrays ending at j to our answer
            total_sum = (total_sum + s2[1]) % MOD

            last_seen[nums[j]] = j
            
        return total_sum