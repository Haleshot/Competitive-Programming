# Roman to Integer (Easy)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Learn: Roman Numerals](#learn-roman-numerals)
- [Solution](#solution)
- [Code Explanation](#code-explanation)
- [Complexity Analysis](#complexity-analysis)
- [Related Resources](#related-resources)

## Problem Statement

[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Given a roman numeral, convert it to an integer.

## Examples

**Example 1:**
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 3:**
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Constraints

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Learn: Roman Numerals

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written largest to smallest from left to right. However, there are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

The mathematical representation of a roman numeral can be expressed as:

$$
\text{Value} = \sum_{i=1}^{n} \begin{cases} 
v_i & \text{if } v_i \geq v_{i+1} \\
-v_i & \text{if } v_i < v_{i+1}
\end{cases}
$$

Where $v_i$ is the value of the $i$-th symbol in the roman numeral string.

## Solution

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            'L' : 50,
            "C" : 100,
            'D' : 500,
            "M":  1000
            }
        # print(d.keys(), "\n", d.values())
        summ = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
                summ += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        return summ
```

## Code Explanation

1. We start by creating a dictionary `d` that maps each Roman numeral symbol to its corresponding integer value.

2. Initialize a variable `summ` to 0, which will store the final integer result.

3. Use a while loop to iterate through the string `s`:
   - If the current symbol's value is less than the next symbol's value (and we're not at the end of the string), we subtract the current symbol's value from the next symbol's value and add the result to `summ`. This handles cases like IV (4) and IX (9).
   - Otherwise, we simply add the current symbol's value to `summ`.

4. Return the final value of `summ`.

This solution efficiently handles the subtraction cases (IV, IX, XL, XC, CD, CM) by comparing adjacent symbols and adjusting the sum accordingly.

## Complexity Analysis

- Time Complexity: O(N), where N is the length of the input string. We iterate through the string once.
- Space Complexity: O(1), as we use a fixed-size dictionary and a constant amount of extra space.

## Related Resources

- [Solution on LeetCode](https://leetcode.com/problems/roman-to-integer/submissions/1356676550/)
- [Explanation of Solution on LeetCode](https://leetcode.com/problems/roman-to-integer/solutions/5640909/roman-to-integer-solution)
- [YouTube Explanation](https://www.youtube.com/watch?v=JlVOzbOJiv0)
- [GitHub Repository with More Solutions](https://github.com/gahogg/Leetcode-Solutions/blob/main/Is%20Subsequence%20-%20Leetcode%20392)

> [!NOTE]
> This problem is part of a larger collection following the roadmap on [algomap.io](https://algomap.io/). For more details and related problems, please refer to the AlgoMap website.
