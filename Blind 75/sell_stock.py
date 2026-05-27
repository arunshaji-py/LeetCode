class Solution:
    def maxProfit(self,prices: list[int]) -> int:
        min_price = prices[0]
        max_price = 0

        #check to find the max price
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_price = max( profit, max_price)

        return max_price
            
