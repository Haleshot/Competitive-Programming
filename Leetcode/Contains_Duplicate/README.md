# Contains Duplicate (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: Counting Occurrences (Time Limit Exceeded)](#approach-1-counting-occurrences-time-limit-exceeded)
  - [Approach 2: Using a Dictionary](#approach-2-using-a-dictionary)
- [Complexity Analysis](#complexity-analysis)
- [Code Explanation](#code-explanation)
- [Related Resources](#related-resources)

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

- [View on Neetcode.io](https://neetcode.io/problems/duplicate-integer)
- [View on LeetCode](https://leetcode.com/problems/contains-duplicate/)

## Examples

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Constraints

- $1 \leq nums.length \leq 10^5$
- $-10^9 \leq nums[i] \leq 10^9$

## Solutions

### Approach 1: Counting Occurrences (Time Limit Exceeded)

```python
class Solution(object):
    def containsDuplicate(self, nums):
        c = 0
        for i in nums:
            if nums.count(i) > 1:
                c += 1
        if c > 1:
            return True
        else:
            return False
```

### Approach 2: Using a Dictionary

```python
class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        result = [i for i in d.values() if i > 1]
        return len(result) >= 1
```

## Complexity Analysis

### Approach 1:
- Time Complexity: $O(n^2)$, where n is the length of the input array.
- Space Complexity: $O(1)$

### Approach 2:
- Time Complexity: $O(n)$, where n is the length of the input array.
- Space Complexity: $O(n)$ in the worst case, where all elements are unique.

## Code Explanation

### Approach 1: Counting Occurrences
This approach iterates through each element in the array and counts its occurrences. If any element occurs more than once, it returns `True`. However, this solution is inefficient for large arrays and can lead to a Time Limit Exceeded error on platforms like LeetCode.

### Approach 2: Using a Dictionary
This solution uses a dictionary to keep track of the count of each element:
1. We iterate through the array, adding each element to the dictionary.
2. If an element is already in the dictionary, we increment its count.
3. After populating the dictionary, we create a list of counts greater than 1.
4. If this list has any elements (length >= 1), it means we have found duplicates, so we return `True`. Otherwise, we return `False`.

This approach is more efficient and passes on both Neetcode.io and LeetCode.

## Related Resources

- [Neetcode Solution](https://github.com/neetcode-gh/leetcode/blob/main/python/0217-contains-duplicate.py)
- [LeetCode Solution](https://leetcode.com/problems/contains-duplicate/solutions/5687332/solution)
- [Personal Submission](https://leetcode.com/submissions/detail/1367496277/)
- [Video Explanation (Neetcode)](https://youtu.be/3OamzN90kPg)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [Neetcode Roadmap](https://neetcode.io/roadmap). For more details and related problems, please refer to the Neetcode.io website.
