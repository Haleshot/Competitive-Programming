class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # Step 1:
        # cheapest_choice, maxP = float('inf'), 0
        # for price in prices:
        #     if price < cheapest_choice:
        #         cheapest_choice = price
        #     profit = price - cheapest_choice
        #     if profit > maxP:
        #         maxP = max(profit, maxP)
        # return maxP

        # # Step 2:
        left, right = 0, 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(profit, maxP)
            else:
                left = right
            right += 1
        return maxP
