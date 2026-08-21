class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            current_profit = prices[r] - prices[l]

            if current_profit < 0:
                l = r


            r += 1
            max_profit = max(current_profit , max_profit)
            
        return max_profit
        