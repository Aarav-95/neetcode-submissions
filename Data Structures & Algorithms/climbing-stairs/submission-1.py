class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        elif n == 3:
            return 3
        elif n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)