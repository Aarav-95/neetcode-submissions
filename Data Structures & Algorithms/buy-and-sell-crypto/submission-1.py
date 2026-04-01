class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            temp = prices[r] - prices[l]
            if temp > profit:
                profit = temp
            if prices[l] > prices[r]:
                l += 1
            else:
                r += 1
        return profit