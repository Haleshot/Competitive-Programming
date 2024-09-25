# 228. Summary Ranges

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: Iterative Range Building](#approach-1-iterative-range-building)
  - [Approach 2: Grouping Consecutive Numbers](#approach-2-grouping-consecutive-numbers)
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

### Example 1

```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

### Example 2

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

### Approach 2: Grouping Consecutive Numbers

```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges, r = [], []
        for num in nums:
            if num - 1 not in r:
                r = []
                ranges.append(r),
            r[1:] = num,
        return ["->".join(map(str, r)) for r in ranges]
```

## Code Explanation

### Approach 1: Iterative Range Building

This approach iterates through the array, identifying consecutive ranges:

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

### Approach 2: Grouping Consecutive Numbers

This approach uses a clever grouping technique:

1. Initialize empty lists `ranges` and `r`.
2. Iterate through each number `num` in `nums`:
   - If `num - 1` is not in `r`, it means we've found the start of a new range:
     - Create a new empty list `r`.
     - Append `r` to `ranges`.
   - Add `num` to `r` using slice assignment `r[1:] = num,`.
3. Convert each range `r` in `ranges` to a string:
   - If `r` has one element, it becomes a single number string.
   - If `r` has two elements, it becomes a "start->end" string.
4. Return the list of formatted range strings.

The key insight in Approach 2 is the use of `r[1:] = num,`. This clever trick ensures that:

- If `r` is empty, `num` becomes the first (and only) element.
- If `r` already has elements, `num` becomes the second element, effectively updating the end of the range.

## Complexity Analysis

Both approaches have the same complexity:

- Time Complexity: O(N), where N is the length of the input array `nums`. We iterate through the array once.
- Space Complexity: O(1), excluding the space used for the output. We only use a constant amount of extra space for variables.

Approach 2 might be slightly more concise and potentially more efficient in terms of code execution, but both solutions are valid and solve the problem effectively.

## Related Resources

- [YouTube Explanation](https://youtu.be/ZHJDwbfqoa8?si=HFic_okEDILM88DC)
- [GitHub Solution](https://github.com/gahogg/Leetcode-Solutions/tree/main/Summary%20Ranges%20-%20Leetcode%20228)
- [LeetCode Submission](https://leetcode.com/submissions/detail/1397595464/)
- [LeetCode Solution Explanation](https://leetcode.com/problems/summary-ranges/solutions/5816924/solution)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
