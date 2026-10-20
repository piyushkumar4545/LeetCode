class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        # Check every divisor k of n.
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            prev = float('-inf')
            possible = True

            for start in range(0, n, k):
                end = start + k

                # Count cyclic descents in this block.
                descents = 0
                for i in range(start, end):
                    j = start if i + 1 == end else i + 1
                    if nums[i] > nums[j]:
                        descents += 1

                if descents > 1:
                    possible = False
                    break

                # Find the minimum possible first element and
                # corresponding last element among sorted rotations.
                first = None
                last = None

                for i in range(start, end):
                    j = start if i + 1 == end else i + 1
                    if nums[i] > nums[j]:
                        first = nums[j]
                        last = nums[i]
                        break

                if first is None:
                    first = nums[start]
                    last = nums[end - 1]

                if first < prev:
                    possible = False
                    break

                prev = last

            if possible:
                ans += k

        return ans