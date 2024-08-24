# 14. Longest Common Prefix (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Approach](#approach)
- [Solutions](#solutions)
  - [Solution 1: Sorting and Comparing](#solution-1-sorting-and-comparing)
  - [Solution 2: Character-by-Character Comparison](#solution-2-character-by-character-comparison)
- [Complexity Analysis](#complexity-analysis)
- [Code Explanation](#code-explanation)
- [Related Resources](#related-resources)

## Problem Statement

[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Examples

### Example 1:

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2:

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Constraints

- $1 \leq strs.length \leq 200$
- $0 \leq strs[i].length \leq 200$
- `strs[i]` consists of only lowercase English letters.

## Approach

We'll explore two different approaches to solve this problem:

1. Sorting and comparing the first and last strings.
2. Character-by-character comparison of all strings.

## Solutions

### Solution 1: Sorting and Comparing

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        strs = sorted(strs)
        min_len, max_len = strs[0], strs[-1]
        for i in range(min(len(min_len), len(max_len))):
            if min_len[i] != max_len[i]:
                return ans
            ans += min_len[i]
        return ans
```

### Solution 2: Character-by-Character Comparison

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return strs[0][:i]
```

## Complexity Analysis

### Solution 1:
- Time Complexity: $O(N \log N + M)$, where N is the number of strings and M is the length of the shortest string.
- Space Complexity: $O(1)$ (excluding the space used for sorting)

### Solution 2:
- Time Complexity: $O(S)$, where S is the sum of all characters in all strings.
- Space Complexity: $O(1)$

## Code Explanation

### Solution 1: Sorting and Comparing
1. Sort the input array of strings lexicographically.
2. Compare the first (lexicographically smallest) and last (lexicographically largest) strings.
3. Build the common prefix until a mismatch is found or we reach the end of either string.

### Solution 2: Character-by-Character Comparison
1. Find the length of the shortest string in the array.
2. Compare characters at each position for all strings.
3. If a mismatch is found, return the common prefix up to that point.
4. If no mismatch is found, return the entire shortest string.

## Related Resources

- [YouTube Explanation](https://www.youtube.com/watch?v=8C6F8_nM0qs)
- [GitHub Solution](https://github.com/gahogg/Leetcode-Solutions/blob/main/Longest%20Common%20Prefix%20-%20Leetcode%2014/Longest%20Common%20Prefix%20-%20Leetcode%2014.py)
- [LeetCode Solution](https://leetcode.com/problems/longest-common-prefix/solutions/5684830/solution/)
- [Personal Submission](https://leetcode.com/submissions/detail/1366878699/)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
