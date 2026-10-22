from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[0]

        # Case 1: Increasing cyclic order
        # nums[i] == (first + i) % n
        if all(nums[i] == (first + i) % n for i in range(n)):
            if first == 0:
                return 0
            return min(n - first, first + 2)

        if all(nums[i] == (first - i) % n for i in range(n)):
            shift = (n - 1 - first) % n
            return 1 + min(shift, n - shift)

        return -1