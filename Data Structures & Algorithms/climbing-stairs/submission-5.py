class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i, memo):
            if memo[i]:
                return memo[i]
            if i == 1:
                result = 1
            elif i == 2:
                result = 2
            else:
                result = dp(i-1, memo) + dp(i-2, memo)
            memo[i] = result
            return result
        
        l = [0] * (n+1)
        return dp(n,l)