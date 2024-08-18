# Best Time to Buy and Sell Stock (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: One-Pass](#approach-1-one-pass)
  - [Approach 2: Two-Pointer](#approach-2-two-pointer)
- [Code Explanation](#code-explanation)
- [Complexity Analysis](#complexity-analysis)
- [Related Resources](#related-resources)

## Problem Statement

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Examples

### Example 1:

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

### Example 2:

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## Constraints

- 1 ≤ prices.length ≤ 10^5
- 0 ≤ prices[i] ≤ 10^4

## Solutions

```python
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
```

### Approach 1: One-Pass

This approach involves iterating through the prices array once, keeping track of the minimum price seen so far and updating the maximum profit if a higher profit is found.

### Approach 2: Two-Pointer

This approach uses two pointers to keep track of the buying and selling days, moving the pointers based on the profit calculation.

## Code Explanation

### Approach 1: One-Pass (Commented Out)

1. Initialize `cheapest_choice` to positive infinity and `maxP` (maximum profit) to 0.
2. Iterate through each price in the `prices` array:
   - If the current price is less than `cheapest_choice`, update `cheapest_choice`.
   - Calculate the potential profit by subtracting `cheapest_choice` from the current price.
   - Update `maxP` if the calculated profit is greater.
3. Return the maximum profit `maxP`.

### Approach 2: Two-Pointer (Active Code)

1. Initialize two pointers: `left` (buying day) at index 0 and `right` (selling day) at index 1.
2. Initialize `maxP` (maximum profit) to 0.
3. While `right` is within the array bounds:
   - If the price at `left` is less than the price at `right`, calculate the profit and update `maxP` if necessary.
   - If the price at `left` is greater or equal to the price at `right`, move `left` to `right` (new potential buying day).
   - Move `right` to the next day.
4. Return the maximum profit `maxP`.

## Complexity Analysis

- Time Complexity: O(n), where n is the number of prices in the array.
- Space Complexity: O(1), as we only use a constant amount of extra space.

## Related Resources

- [LeetCode Submission](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1360165286)
- [Detailed Explanation](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/5655153/solution/)
- [AlgoMap YouTube Explanation](https://www.youtube.com/watch?v=kJZrMGpyWpk)
- [NeetCode YouTube Explanation](https://www.youtube.com/watch?v=1pkOgXD63yU&t=426s)
- [GitHub Implementation](https://github.com/gahogg/Leetcode-Solutions/blob/main/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20-%20Leetcode%20121/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20-%20Leetcode%20121.py)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
