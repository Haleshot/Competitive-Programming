# Longest Common Prefix (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Solution 1: Sorting Approach](#solution-1-sorting-approach)
  - [Solution 2: Character-by-Character Comparison](#solution-2-character-by-character-comparison)
- [Complexity Analysis](#complexity-analysis)
- [Code Explanation](#code-explanation)
- [Additional Resources](#additional-resources)

## Problem Statement

[Longest Common Prefix - LeetCode](https://leetcode.com/problems/longest-common-prefix/description/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

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

- $$1 \leq \text{strs.length} \leq 200$$
- $$0 \leq \text{strs[i].length} \leq 200$$
- $$\text{strs[i]}$$ consists of only lowercase English letters.

## Solutions

### Solution 1: Sorting Approach

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
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
        """
        :type strs: List[str]
        :rtype: str
        """
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

### Solution 1: Sorting Approach
- Time Complexity: $$O(N \log N + M)$$, where $$N$$ is the number of strings and $$M$$ is the length of the longest string.
- Space Complexity: $$O(1)$$ (ignoring the space used for sorting)

### Solution 2: Character-by-Character Comparison
- Time Complexity: $$O(S)$$, where $$S$$ is the sum of all characters in all strings.
- Space Complexity: $$O(1)$$

## Code Explanation

### Solution 1: Sorting Approach

1. Sort the array of strings lexicographically.
2. Compare the first and last strings in the sorted array.
3. The longest common prefix will be the common prefix of these two strings.

### Solution 2: Character-by-Character Comparison

1. Find the length of the shortest string in the array.
2. Iterate through the characters of the first string up to the length of the shortest string.
3. For each character, compare it with the corresponding character in all other strings.
4. If a mismatch is found, return the prefix up to that point.
5. If no mismatch is found, return the entire shortest string as the longest common prefix.

## Additional Resources

- [YouTube Explanation - Algomap](https://www.youtube.com/watch?v=8C6F8_nM0qs)
- [GitHub - Leetcode Solutions](https://github.com/gahogg/Leetcode-Solutions/blob/main/Longest%20Common%20Prefix%20-%20Leetcode%2014/Longest%20Common%20Prefix%20-%20Leetcode%2014.py)
- [LeetCode Solution Explanation](https://leetcode.com/problems/longest-common-prefix/solutions/5684830/solution/)
- [Personal Submission Details](https://leetcode.com/submissions/detail/1366878699/)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
