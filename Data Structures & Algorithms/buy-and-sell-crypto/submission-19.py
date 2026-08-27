class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_value = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            
            else:
                max_value = max(max_value , prices[r] - prices[l])
            r += 1
        return max_value
            
        