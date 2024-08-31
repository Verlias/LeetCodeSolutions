class Solution(object):
    def maxProfit(self, prices):
        best_profit = 0

        min_price = prices[0]

        for i in range(1, len(prices)):
            #If current index value is less than the min_price. update min_price
            if prices[i] < min_price:
                min_price = prices[i]
            #If the current index value is greater than the min_price. Calculate profit
            best_profit = max(best_profit, prices[i] - min_price)

        return best_profit




        
        