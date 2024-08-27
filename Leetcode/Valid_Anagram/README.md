# Valid Anagram (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: Using Two Dictionaries](#approach-1-using-two-dictionaries)
  - [Approach 2: Using Two dictionaries separately](#approach-2-using-two-dictionaries-separately)
- [Complexity Analysis](#complexity-analysis)
- [Code Explanation](#code-explanation)
- [Related Resources](#related-resources)

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

- [View on Neetcode.io](https://neetcode.io/problems/is-anagram)
- [View on LeetCode](https://leetcode.com/problems/valid-anagram/description/)

## Examples

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
```

## Constraints

- $1 \leq s.length, t.length \leq 5 \times 10^4$
- `s` and `t` consist of lowercase English letters.

## Solutions

### Approach 1: Using Two Dictionaries

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
```

This solution checks if the two strings have the same character counts. It uses two dictionaries (`countS` and `countT`) to count the frequency of each character in `s` and `t`. If the dictionaries are equal, then `t` is an anagram of `s`.

**Note:** This approach works efficiently for Neetcode.io but may result in a Time Limit Exceeded (TLE) error on LeetCode for some test cases due to the double dictionary comparison.

### Approach 2: Using Two dictionaries separately

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        countS, countT = dict(), dict()
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
```

This solution also uses two dictionaries (`countS` and `countT`) but separates the loops for counting characters in `s` and `t`. By building the frequency counts in separate loops, it ensures each string is fully processed before the comparison. This approach passes on both Neetcode.io and LeetCode.

## Complexity Analysis

### Approach 1: Using Two Dictionaries

- **Time Complexity:** $O(n)$, where \( n \) is the length of the string `s` (or `t`, since they are equal in length). The loop runs through each character in `s` and `t` once, and the dictionary comparison is also linear.
- **Space Complexity:** $O(1)$ because the dictionaries can only store a maximum of 26 characters (lowercase English letters).

### Approach 2: Using a Single Dictionary

- **Time Complexity:** $O(n)$, where \( n \) is the length of the string `s` or `t`. Similar to the first approach, the time complexity is linear due to the dictionary operations.
- **Space Complexity:** $O(1)$ for the same reason as above—the dictionaries store at most 26 different characters.

## Code Explanation

### Approach 1: Using Two Dictionaries

This approach involves creating two dictionaries, `countS` and `countT`, to keep track of the frequency of each character in the strings `s` and `t`, respectively. We iterate over each character in both strings simultaneously, updating the dictionaries. Finally, we check if both dictionaries are equal. If they are, the function returns `True`, indicating that `t` is an anagram of `s`; otherwise, it returns `False`.

### Approach 2: Using a Single Dictionary

This method separates the process into two loops: one for counting the characters in `s` and the other for `t`. After populating both dictionaries, it compares them. This approach also ensures that both strings are processed completely before making the comparison.

## Related Resources

- [Neetcode Solution](https://github.com/neetcode-gh/leetcode/blob/main/python/0242-valid-anagram.py)
- [LeetCode Solution](https://leetcode.com/problems/contains-duplicate/submissions/1367496277)
- [Video Explanation (Neetcode)](https://youtu.be/9UtInBqnCgA?si=ZNIBKu_UKmbwXL-v)
- [LeetCode Solution Discussion](https://leetcode.com/problems/valid-anagram/solutions/5699383/solution)
- [Personal Submission](https://leetcode.com/submissions/detail/1370348068/)

> **Note:** This problem is part of a collection that helps you understand anagrams and string manipulation techniques. Check out the [Neetcode Roadmap](https://neetcode.io/roadmap) for more problems and detailed solutions.
