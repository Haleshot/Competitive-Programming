# Two Sum (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: Brute Force (Time Limit Exceeded)](#approach-1-brute-force-time-limit-exceeded)
  - [Approach 2: Hash Map](#approach-2-hash-map)
- [Complexity Analysis](#complexity-analysis)
- [Code Explanation](#code-explanation)
- [Related Resources](#related-resources)

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

- [View on Neetcode.io](https://neetcode.io/problems/two-integer-sum)
- [View on LeetCode](https://leetcode.com/problems/two-sum/description/)

## Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- $2 \leq nums.length \leq 10^4$
- $-10^9 \leq nums[i] \leq 10^9$
- $-10^9 \leq target \leq 10^9$
- Only one valid answer exists.

## Solutions

### Approach 1: Brute Force (Time Limit Exceeded)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    if nums.index(nums[i]) == nums.index(nums[j]):
                        return [nums.index(nums[i]), nums.index(nums[j], i + 1, len(nums))]
                    return [nums.index(nums[i]), nums.index(nums[j])]
```

### Approach 2: Hash Map

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seenMap:
                return [seenMap[remain], i]
            seenMap[nums[i]] = i
        return []
```

## Complexity Analysis

### Approach 1: Brute Force
- Time Complexity: $O(n^2)$, where n is the length of the input array.
- Space Complexity: $O(1)$

### Approach 2: Hash Map
- Time Complexity: $O(n)$, where n is the length of the input array.
- Space Complexity: $O(n)$

## Code Explanation

### Approach 1: Brute Force
This approach uses nested loops to check every pair of numbers in the array. For each number, it searches for a complementary number that adds up to the target. While straightforward, this method is inefficient for large inputs and can lead to a Time Limit Exceeded error on platforms like LeetCode.

### Approach 2: Hash Map
This solution uses a hash map to store the numbers we've seen and their indices:
1. We iterate through the array once.
2. For each number, we calculate the complement (target - current number).
3. If the complement exists in our hash map, we've found a solution.
4. If not, we add the current number and its index to the hash map.
5. This allows us to find the solution in a single pass through the array.

This approach is more efficient and passes on both Neetcode.io and LeetCode.

## Related Resources

- [Neetcode Solution](https://github.com/neetcode-gh/leetcode/blob/main/python/0001-two-sum.py)
- [LeetCode Solution](https://leetcode.com/problems/two-sum/solutions/5708451/solution)
- [Personal Submission](https://leetcode.com/submissions/detail/1372537730/)
- [Video Explanation (Neetcode)](https://youtu.be/KLlXCFG5TnA?si=SNCJAwAEYqfQUAtv)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [Neetcode Roadmap](https://neetcode.io/roadmap). For more details and related problems, please refer to the Neetcode.io website.
