# Group Anagrams (Medium)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Solutions](#solutions)
  - [Approach 1: Using Sorted Strings as Keys](#approach-1-using-sorted-strings-as-keys)
  - [Approach 2: Hash Map with Character Count as Key](#approach-2-hash-map-with-character-count-as-key)
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

### Approach 1: Using Sorted Strings as Keys

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

### Approach 2: Hash Map with Character Count as Key

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seenMap:
                return [seenMap[remain], i]
            seenMap[nums[i]] = i
        return nums
```

## Complexity Analysis

### Approach 1:
- Time Complexity: $O(N * M * \log(M))$, where N is the number of strings and M is the maximum length of a string.
- Space Complexity: $O(N * M)$

### Approach 2:
- Time Complexity: $O(N * M)$, where N is the number of strings and M is the maximum length of a string.
- Space Complexity: $O(N * M)$

## Code Explanation

### Approach 1: Using Sorted Strings as Keys
This approach involves sorting each string and using the sorted string as a key in a dictionary. 

### Approach 2: Hash Map with Character Count as Key
This solution uses a hash map to group anagrams:
1. We iterate through each string in the input array.
2. For each string, we create a key by counting the occurrences of each character.
3. We use this count as a key in our hash map. The value is a list of all strings that have the same character count.
4. Finally, we return the values of the hash map, which are the grouped anagrams.

This approach is efficient and passes on both Neetcode.io and LeetCode.

## Related Resources

- [Neetcode Solution](https://github.com/neetcode-gh/leetcode/blob/main/python/0049-group-anagrams.py)
- [LeetCode Solution](https://leetcode.com/problems/group-anagrams/solutions/5729062/solution)
- [Personal Submission](https://leetcode.com/submissions/detail/1377240624/)
- [Video Explanation (Neetcode)](https://youtu.be/vzdNOK2oB2E?si=aFbSKVZz4WfzrNg1)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [Neetcode Roadmap](https://neetcode.io/roadmap). For more details and related problems, please refer to the Neetcode.io website.
