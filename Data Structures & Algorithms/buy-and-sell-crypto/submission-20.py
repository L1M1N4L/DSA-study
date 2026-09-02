class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_value = 0
        while r < len(prices):
            current_count = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            r += 1
            max_value = max(max_value , current_count)
        return max_value