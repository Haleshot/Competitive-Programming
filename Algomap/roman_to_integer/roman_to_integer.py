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
        print(d.keys(), "\n", d.values())
        sum = 0
        
        for i in s:
            sum += d[i]
        return sum