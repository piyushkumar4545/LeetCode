class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        while n >= stones:
            n -= stones
            stones -= 1
        return stones % 2 == 1