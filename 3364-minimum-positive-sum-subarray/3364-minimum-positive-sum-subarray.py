class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(n):
            for length in range(l, r + 1):
                if i + length <= n:
                    s = prefix[i + length] - prefix[i]
                    if s > 0:
                        ans = min(ans, s)

        return ans if ans != float('inf') else -1