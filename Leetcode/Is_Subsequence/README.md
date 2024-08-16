# Is Subsequence (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Follow-up](#follow-up)
- [Solutions](#solutions)
  - [Two-Pointer Approach](#two-pointer-approach)
- [Code Explanation](#code-explanation)
- [Complexity Analysis](#complexity-analysis)
- [Related Resources](#related-resources)

## Problem Statement

[Is Subsequence](https://leetcode.com/problems/is-subsequence/)

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Examples

### Example 1:

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

### Example 2:

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

## Constraints

- 0 ≤ s.length ≤ 100
- 0 ≤ t.length ≤ 10^4
- `s` and `t` consist only of lowercase English letters.

## Follow-up

Suppose there are lots of incoming `s`, say $s_1, s_2, ..., s_k$ where $k \geq 10^9$, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

## Solutions

### Two-Pointer Approach

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Step 1
        if not s:
            return True

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)
```

## Code Explanation

The solution uses a two-pointer approach to solve the problem efficiently:

1. First, we check if the string `s` is empty. If it is, we return `True` because an empty string is always a subsequence of any string.

2. We initialize two pointers, `i` for string `s` and `j` for string `t`.

3. We iterate through both strings simultaneously:
   - If the characters at `s[i]` and `t[j]` match, we move the `i` pointer forward.
   - Regardless of whether there's a match or not, we always move the `j` pointer forward.

4. We continue this process until we reach the end of either `s` or `t`.

5. Finally, we check if `i` has reached the end of `s`. If it has, it means we've found all characters of `s` in `t` in the correct order, so we return `True`. Otherwise, we return `False`.

This approach ensures that we only need to traverse both strings once, making it an efficient solution.

## Complexity Analysis

- Time Complexity: O(T), where T is the length of string `t`. In the worst case, we might need to iterate through the entire string `t`.
- Space Complexity: O(1), as we only use two pointers and don't require any additional data structures that grow with input size.

## Related Resources

- [YouTube Explanation](https://www.youtube.com/watch?v=M_OB20n4hfo)
- [GitHub Implementation](https://github.com/gahogg/Leetcode-Solutions/blob/main/Is%20Subsequence%20-%20Leetcode%20392)
- [LeetCode Submission](https://leetcode.com/submissions/detail/1357387663/)
- [LeetCode Solution Explanation](https://leetcode.com/problems/is-subsequence/solutions/5643649/is-subsequence-solution)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
