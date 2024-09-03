# Anagram Groups (Medium)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: Sorting Characters](#approach-1-sorting-characters)
  - [Approach 2: Character Count](#approach-2-character-count)
- [Complexity Analysis](#complexity-analysis)
- [Code Explanation](#code-explanation)
- [Related Resources](#related-resources)

## Problem Statement

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

- [View on Neetcode.io](https://neetcode.io/problems/anagram-groups)
- [View on LeetCode](https://leetcode.com/problems/group-anagrams/description/)

## Examples

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- $1 \leq strs.length \leq 10^4$
- $0 \leq strs[i].length \leq 100$
- `strs[i]` consists of lowercase English letters.

## Solutions

### Approach 1: Sorting Characters

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())
```

### Approach 2: Character Count

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
```

## Complexity Analysis

### Approach 1: Sorting Characters
- Time Complexity: $O(N * M * log(M))$, where N is the number of strings and M is the maximum length of a string.
- Space Complexity: $O(N * M)$

### Approach 2: Character Count
- Time Complexity: $O(N * M)$, where N is the number of strings and M is the maximum length of a string.
- Space Complexity: $O(N * M)$

## Code Explanation

### Approach 1: Sorting Characters
1. We use a defaultdict to group anagrams.
2. For each word, we sort its characters to create a key.
3. We append the original word to the list associated with its sorted key.
4. Finally, we return the values of the dictionary as a list of lists.

### Approach 2: Character Count
1. We use a defaultdict to group anagrams.
2. For each word, we create a count array of length 26 (for lowercase English letters).
3. We count the occurrences of each character in the word.
4. We use the tuple of this count array as a key to group anagrams.
5. We append the original word to the list associated with its count key.
6. Finally, we return the values of the dictionary.

## Related Resources

- [Neetcode Solution](https://github.com/neetcode-gh/leetcode/blob/main/python/0049-group-anagrams.py)
- [LeetCode Solution](https://leetcode.com/problems/group-anagrams/solutions/5729062/solution)
- [Personal Submission](https://leetcode.com/submissions/detail/1377240624/)
- [Video Explanation (Neetcode)](https://youtu.be/vzdNOK2oB2E?si=aFbSKVZz4WfzrNg1)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [Neetcode Roadmap](https://neetcode.io/roadmap). For more details and related problems, please refer to the Neetcode.io website.
