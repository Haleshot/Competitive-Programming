class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pos, neg = [i for i in nums if i > 0], [i for i in nums if i < 0]
        min_pos, max_neg = min(pos), max(neg)
        print(min_pos, "\n", max_neg)
        return max(min_pos, max_neg)
        