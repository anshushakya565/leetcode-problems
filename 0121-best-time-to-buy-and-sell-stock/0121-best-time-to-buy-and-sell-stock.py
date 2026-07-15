class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        minPrice = prices[0]
        for i in prices:
            if minPrice > i:
                minPrice = i
            else:
                profit = i - minPrice
                if profit > maxpro:
                    maxpro = profit
        return maxpro