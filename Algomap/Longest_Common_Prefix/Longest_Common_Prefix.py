class Solution(object):
    def longestCommonPrefix(self, strs=None):
        """
        :type strs: List[str]
        :rtype: str
        """
        # for i in strs:
        #     c = 0
        #     long_com_pre = ""
        #     flag = True
        #     while flag:
        #         long_com_pre += i[c]
        #         other = [j for j in strs[strs.index(i):strs]]
        #         if long_com_pre in others:
        #             continue
        #         else:
        #             flag = False
        #             break
        #         c += 1
        # return long_com_pre
    
        log = ["flower", "flight", "flowing", "flight", "floom"]
        if "f" in log:
            print("True")
        else:
            print("False")

param1 = ["flower","flow","flight"]
   
Solution.longestCommonPrefix(param1)