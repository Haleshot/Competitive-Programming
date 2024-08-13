class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # # Step 1
        mergedword = ""
        if len(word1) < len(word2):
            for i in range(len(word1)):
                mergedword += word1[i] + word2[i]
            mergedword += word2[len(word1):len(word2)]
            return mergedword
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                mergedword += word1[i] + word2[i]
            mergedword += word1[len(word2):len(word1)]
            return mergedword
        else:
            for i in range(len(word2)):
                mergedword += word1[i] + word2[i]
            return mergedword

        # # Step 2
        # result = []
        # i = 0
        # while i < len(word1) or i < len(word2):
        #     if i < len(word1):
        #         result.append(word1[i])
        #     if i < len(word2):
        #         result.append(word2[i])
        #     i += 1
        # return ''.join(result)