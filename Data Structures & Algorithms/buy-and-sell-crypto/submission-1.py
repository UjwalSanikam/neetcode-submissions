class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        max_profit = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i+1, len(prices)):
                profit = prices[j] - buy_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
