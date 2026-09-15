class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 # Buy low, sell high
        lowestPrice = prices[0]

        for value in prices[1:]:
            profit = value - lowestPrice
            maxProfit = max(maxProfit, profit)

            lowestPrice = min(lowestPrice, value)
        return maxProfit