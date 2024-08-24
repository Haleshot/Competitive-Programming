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
        