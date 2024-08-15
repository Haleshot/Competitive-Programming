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
        sum = 0
        # for i in s:
        #     temp =  s.index(i) + 1
        #     print(temp)
        #     next = s[temp]
        #     if d[i] > d[next]:
        #         sum += d[next] - d[i]
        #     sum += d[i]

        for i in range(len(s)):
            print(d[s[i + 1]])
            if d[s[i]] < d[s[i + 1]]:
                sum += d[s[i + 1]] - d[s[i]]
            sum += d[s[i]]
        return sum
        