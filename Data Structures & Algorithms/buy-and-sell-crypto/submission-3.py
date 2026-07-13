class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r , l = 1 , 0
        maxprofit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            maxprofit = max(prices[r] - prices[l] , maxprofit)
            r += 1
        return maxprofit