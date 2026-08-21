class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        l = 0
        res = 0
        while r < len(prices):
            current_price = prices[r] - prices[l]
            if current_price < 0:
                l = r
            r += 1
            res = max(current_price , res)
        return res