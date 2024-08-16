class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
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
