class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # highest buy price var that updates
        # pointer for buy price
        # pointer for sale price

        buyDay = 0
        saleDay = 0
        profit = 0

        for buyDay in range(len(prices)-1):
            for saleDay in range(buyDay+1, len(prices)):
                if prices[buyDay] < prices[saleDay] and saleDay != len(prices):
                    profit = max(profit, prices[saleDay] - prices[buyDay])
        return profit





        