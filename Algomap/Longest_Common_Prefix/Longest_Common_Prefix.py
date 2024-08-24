class Solution(object):
    def longestCommonPrefix(self, strs=None):
        """
        :type strs: List[str]
        :rtype: str
        """
        # # Step 1
        ans = ""
        strs = sorted(strs)
        min_len, max_len = strs[0], strs[-1]
        for i in range(min(len(min_len), len(max_len))):
            if min_len[i] != max_len[i]:
                return ans
            ans += min_len[i]
        return ans

        # # Step 2:
        # min_length = float('inf')

        # for s in strs:
        #     if len(s) < min_length:
        #         min_length = len(s)

        # i = 0
        # while i < min_length:
        #     for s in strs:
        #         if s[i] != strs[0][i]:
        #             return s[:i]
        #     i += 1

        # return strs[0][:i]
