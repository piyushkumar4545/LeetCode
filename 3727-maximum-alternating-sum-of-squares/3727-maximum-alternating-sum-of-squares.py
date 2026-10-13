class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        squares = [x * x for x in nums]
        
        n = len(nums)
        k = (n + 1) // 2
        
        return sum(squares[n - k:]) - sum(squares[:n - k])