# Neetcode
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # # Step 1
        # anagrams = defaultdict(list)  # Initialize a dictionary to hold lists of anagrams
        
        # # Iterate over each word in the list
        # for word in strs:
        #     # Sort the characters of the word to use as the key
        #     sorted_word = ''.join(sorted(word))
        #     # Group anagrams together using the sorted word as the key
        #     anagrams[sorted_word].append(word)
        
        # # Convert the dictionary values (which are lists of anagrams) to a list of lists
        # return list(anagrams.values())

        # # Step 2:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


# Leetcode
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # # Step 1
        # anagrams = defaultdict(list)  # Initialize a dictionary to hold lists of anagrams
        
        # # Iterate over each word in the list
        # for word in strs:
        #     # Sort the characters of the word to use as the key
        #     sorted_word = ''.join(sorted(word))
        #     # Group anagrams together using the sorted word as the key
        #     anagrams[sorted_word].append(word)
        
        # # Convert the dictionary values (which are lists of anagrams) to a list of lists
        # return list(anagrams.values())

        # # Step 2:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

