# 1768. Merge Strings Alternately (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Solution 1: Conditional Merging](#solution-1-conditional-merging)
  - [Solution 2: Simultaneous Iteration (Commented Out)](#solution-2-simultaneous-iteration-commented-out)
- [Complexity Analysis](#complexity-analysis)
- [Additional Resources](#additional-resources)

## Problem Statement

[Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/)

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

## Examples

### Example 1:

```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

### Example 2:

```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
```

### Example 3:

```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

## Constraints

- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.

## Solutions

### Solution 1: Conditional Merging

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mergedword = ""
        if len(word1) < len(word2):
            for i in range(len(word1)):
                mergedword += word1[i] + word2[i]
            mergedword += word2[len(word1):len(word2)]
            return mergedword
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                mergedword += word1[i] + word2[i]
            mergedword += word1[len(word2):len(word1)]
            return mergedword
        else:
            for i in range(len(word2)):
                mergedword += word1[i] + word2[i]
            return mergedword
```

#### Explanation:

1. Initialize an empty string `mergedword` to store the result.
2. Compare the lengths of `word1` and `word2`:
   - If `word1` is shorter:
     - Iterate through the length of `word1`, adding characters alternately.
     - Append the remaining characters of `word2`.
   - If `word2` is shorter:
     - Iterate through the length of `word2`, adding characters alternately.
     - Append the remaining characters of `word1`.
   - If both words are of equal length:
     - Iterate through the length of either word, adding characters alternately.
3. Return the `mergedword`.

### Solution 2: Simultaneous Iteration (Commented Out)

```python
# result = []
# i = 0
# while i < len(word1) or i < len(word2):
#     if i < len(word1):
#         result.append(word1[i])
#     if i < len(word2):
#         result.append(word2[i])
#     i += 1
# return ''.join(result)
```

#### Explanation:

This solution (currently commented out) uses a single loop to iterate through both words simultaneously:

1. Initialize an empty list `result` and a counter `i`.
2. While `i` is less than the length of either word:
   - If `i` is within `word1`'s length, append the character from `word1`.
   - If `i` is within `word2`'s length, append the character from `word2`.
   - Increment `i`.
3. Join the `result` list into a string and return it.

## Complexity Analysis

For Solution 1 (the active solution):

- Time Complexity: O(N), where N is the length of the longer word.
- Space Complexity: O(N) to store the merged word.

## Additional Resources

- [YouTube Explanation](https://youtu.be/qq-AqEPKsI8?si=Cg-NzjPzwucfsrd4)
- [GitHub Solution](https://github.com/gahogg/Leetcode-Solutions/blob/main/Merge%20Strings%20Alternately%20-%20Leetcode%201768)
- [LeetCode Submission](https://leetcode.com/problems/merge-strings-alternately/submissions/1354495470)