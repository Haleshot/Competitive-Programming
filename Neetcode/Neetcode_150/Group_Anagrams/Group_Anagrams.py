# Neetcode
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        for i in strs:
            for j in range(strs.index(i) + 1, len(strs)):
                if sorted(i) == sorted(strs[j]):
                    results.append([i, strs[j]])
        for i in results:
            for j in range(len(i) - 1):
                if i[j] == i[j + 1]:
                    print(i[j])
        return results
