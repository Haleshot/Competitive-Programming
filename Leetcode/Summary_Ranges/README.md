# 228. Summary Ranges

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: Iterative Range Building](#approach-1-iterative-range-building)
- [Code Explanation](#code-explanation)
- [Complexity Analysis](#complexity-analysis)
- [Related Resources](#related-resources)

## Problem Statement

[Summary Ranges](https://leetcode.com/problems/summary-ranges/)

You are given a sorted unique integer array `nums`. A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

## Examples

### Example 1:

```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

### Example 2:

```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

## Constraints

- `0 <= nums.length <= 20`
- $$-2^{31} <= nums[i] <= 2^{31} - 1$$
- All the values of `nums` are unique.
- `nums` is sorted in ascending order.

## Solutions

### Approach 1: Iterative Range Building

```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result, i = [], 0
        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and (nums[i] + 1) == nums[i + 1]:
                i += 1
            if start != nums[i]:
                result.append(str(start) + "->" + str(nums[i]))
            else:
                result.append(str(nums[i]))
            i += 1
        return result
```

## Code Explanation

The `summaryRanges` function works as follows:

1. Initialize an empty list `result` to store the range strings and a counter `i` to iterate through the array.
2. While `i` is less than the length of `nums`:
   - Store the current number as `start`.
   - While the next number is consecutive (current number + 1), increment `i`.
   - If `start` is different from the current number (indicating a range):
     - Append the range as "start->current" to `result`.
   - Otherwise (for single number ranges):
     - Append the number as a string to `result`.
   - Increment `i` to move to the next number.
3. Return the `result` list containing all the ranges.

## Complexity Analysis

- Time Complexity: O(N), where N is the length of the input array `nums`. We iterate through the array once.
- Space Complexity: O(1), excluding the space used for the output. We only use a constant amount of extra space for variables.

## Related Resources

- [YouTube Explanation](https://youtu.be/ZHJDwbfqoa8?si=HFic_okEDILM88DC)
- [GitHub Solution](https://github.com/gahogg/Leetcode-Solutions/tree/main/Summary%20Ranges%20-%20Leetcode%20228)
- [LeetCode Submission](https://leetcode.com/submissions/detail/1397595464/)
- [LeetCode Solution Explanation](https://leetcode.com/problems/summary-ranges/solutions/5816924/solution)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
