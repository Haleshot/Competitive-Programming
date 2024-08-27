# Neetcode
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT


# Leetcode
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
