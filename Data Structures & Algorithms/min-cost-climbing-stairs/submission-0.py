class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, last = cost[-2], cost[-1]
        n = len(cost)
        for i in range(n-3, -1, -1):
            temp = prev
            prev = cost[i] + min(prev, last)
            last = temp
        
        return min(prev, last)