class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        elif 0 in nums:
            return 0
        else:
            pos, neg = [i for i in nums if i > 0], [i for i in nums if i < 0]
            if len(pos) != 0 and len(neg) == 0:
                # print(min(pos))
                return min(pos)
            elif len(pos) == 0 and len(neg) != 0:
                # print(max(neg))
                return max(neg)
            else:
                min_pos, max_neg = min(pos), max(neg)
                if min_pos == abs(max_neg):
                    return min_pos
                else:
                    diff1, diff2 = min_pos, 0 - max_neg
                    if diff1 < diff2:
                        return min_pos
                    return max_neg
