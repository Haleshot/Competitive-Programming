# Product of Array Except Self (Medium)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Optimal Solution](#optimal-solution)
  - [Alternative Solution](#alternative-solution)
- [Code Explanation](#code-explanation)
- [Complexity Analysis](#complexity-analysis)
- [Additional Resources](#additional-resources)

## Problem Statement

[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

### Example 1:

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Example 2:

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints

- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Solutions

### Optimal Solution

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answers = []
        leftptr = 1
        for i in range(len(nums)):
            answers.append(leftptr)
            leftptr *= nums[i]
        
        rightptr = 1
        for i in range(len(nums) - 1, -1, -1):
            answers[i] *= rightptr
            rightptr *= nums[i]
        return answers
```

### Alternative Solution

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bef = [1] * len(nums)
        aft = [1] * len(nums)
        for i in range(1, len(nums)):
            bef[i] = bef[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            aft[i] = aft[i + 1] * nums[i + 1]
        return [bef[i] * aft[i] for i in range(len(nums))]
```

## Code Explanation

### Optimal Solution

The optimal solution uses a two-pass approach to calculate the product of all elements except self:

1. First pass (left to right):
   - Initialize an `answers` list to store the results.
   - Use `leftptr` to keep track of the cumulative product from the left.
   - For each element, append the current `leftptr` to `answers` and update `leftptr` by multiplying it with the current element.

2. Second pass (right to left):
   - Use `rightptr` to keep track of the cumulative product from the right.
   - Iterate from right to left, multiplying each element in `answers` by `rightptr` and updating `rightptr`.

This approach calculates the product of all elements to the left and right of each element without using division.

### Alternative Solution

The alternative solution uses two separate arrays to store the products:

1. `bef` array: Stores the product of all elements to the left of each element.
2. `aft` array: Stores the product of all elements to the right of each element.

The final result is obtained by multiplying corresponding elements from `bef` and `aft`.

## Complexity Analysis

For the optimal solution:
- Time Complexity: O(N), where N is the length of the input array.
- Space Complexity: O(1), excluding the output array.

## Additional Resources

- [YouTube Explanation](https://youtu.be/yKZFurr4GQA?si=-wykJZfdRSw7M8UN)
- [GitHub Solution](https://github.com/gahogg/Leetcode-Solutions/tree/main/Product%20of%20Array%20Except%20Self%20-%20Leetcode%20238)
- [LeetCode Solution Explanation](https://leetcode.com/problems/product-of-array-except-self/solutions/5757573/solution)
- [Personal Submission Details](https://leetcode.com/submissions/detail/1383555855/)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
