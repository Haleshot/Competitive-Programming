# Neetcode
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # Step 1:
        # c = 0
        # for i in nums:
        #     if nums.count(i) > 1:
        #         c += 1
        # if c > 1:
        #     return True
        # else:
        #     return False

        # # Step 2:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        result = [i for i in d.values() if i > 1]
        # print(result)
        return len(result) >= 1


# Leetcode
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # # Step 1 (TLE)
        # c = 0
        # for i in nums:
        #     if nums.count(i) > 1:
        #         c += 1
        # if c > 1:
        #     return True
        # else:
        #     return False

        # # Step 2:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # print(len(d.values()), len(set(d.values())))
        # print(set(nums))
        # return len(d.values()) == len(set(nums))
        result = [i for i in d.values() if i > 1]
        # print(result)
        return len(result) >= 1
