class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        allProfits= []
        
        buyingPrice = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] - buyingPrice < 1:
                buyingPrice = prices[i]
            else:
                allProfits.append(prices[i] - buyingPrice)
        if len(allProfits) > 0:
            return max(allProfits)
        else:
            return 0

