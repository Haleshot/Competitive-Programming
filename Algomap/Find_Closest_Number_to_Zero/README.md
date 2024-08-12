# Find Closest Number to Zero (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solution Approach](#solution-approach)
- [Code Implementation](#code-implementation)
- [Time Complexity](#time-complexity)
- [Space Complexity](#space-complexity)
- [Additional Resources](#additional-resources)

## Problem Statement

[Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero/description/)

Given an integer array `nums` of size `n`, return the number with the value closest to 0 in `nums`. If there are multiple answers, return the number with the largest value.

## Examples

### Example 1:

```
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
```

### Example 2:

```
Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
```

## Constraints

- 1 <= n <= 1000
- -10^5 <= nums[i] <= 10^5

## Solution Approach

The solution uses the following approach:

1. Sort the input array.
2. Handle edge cases:
   - If the array has only one element, return that element.
   - If 0 is in the array, return 0 as it's the closest to itself.
3. Separate positive and negative numbers into two lists.
4. Compare the smallest positive number with the absolute value of the largest negative number.
5. Return the number closest to 0, or the larger one if they are equidistant.

## Code Implementation

```python
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        elif 0 in nums:
            return 0
        else:
            pos, neg = [i for i in nums if i > 0], [i for i in nums if i < 0]
            if len(pos) != 0 and len(neg) == 0:
                return min(pos)
            elif len(pos) == 0 and len(neg) != 0:
                return max(neg)
            else:
                min_pos, max_neg = min(pos), max(neg)
                if min_pos == abs(max_neg):
                    return min_pos
                else:
                    diff1, diff2 = min_pos, 0 - max_neg
                    if diff1 < diff2:
                        return min_pos
                    return max_neg
```

## Time Complexity

The time complexity of this solution is O(N log N), where N is the number of elements in the input array. This is primarily due to the sorting operation at the beginning of the function.

## Space Complexity

The space complexity is O(N) in the worst case, where we might need to store all elements in the `pos` and `neg` lists.

## Additional Resources

- [YouTube Explanation](https://www.youtube.com/watch?v=dLlKA5DQKYs)
- [GitHub - Other Leetcode Solutions](https://github.com/gahogg/Leetcode-Solutions/blob/main/Find%20Closest%20Number%20to%20Zero%20-%20Leetcode%202239)

> [!NOTE] This problem is part of a collection following the roadmap on [algomap.io](https://algomap.io/). 
> This README is part of the AlgoMap-guided problem-solving series in the CP repo.
