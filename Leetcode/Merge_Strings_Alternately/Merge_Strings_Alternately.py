class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
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