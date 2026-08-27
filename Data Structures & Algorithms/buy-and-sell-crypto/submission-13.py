class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxvalue = 0
        
        for i in range(len(prices)):
            for j in range(i+1):
                maxvalue = max(prices[i] - prices[j] , maxvalue)
        return maxvalue
