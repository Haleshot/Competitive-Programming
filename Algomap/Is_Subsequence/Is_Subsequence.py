class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Step 1
        if not s:
            return True

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

        # # Step 2:
        # if s == "": return True
        # if len(s) > len(t): return False

        # j = 0

        # for i in range(len(t)):
        #     if s[j] == t[i]:
        #         if j == len(s) - 1:
        #             return True
        #         j += 1
        # return False
