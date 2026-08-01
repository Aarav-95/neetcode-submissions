class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def dp(i, arr):
            if arr[i] != -1:
                return arr[i]
            if i == n-1 or i == n-2:
                return cost[i]
            return cost[i] + min(dp(i+1, arr), dp(i+2, arr))

        arr = [-1] * n
        for i in range(n-1, -1, -1):
            arr[i] = dp(i, arr)
        return min(arr[0], arr[1])
        