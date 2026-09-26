class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)

        return [
            candies[i] + extraCandies >= max_candies
            for i in range(len(candies))
        ]
