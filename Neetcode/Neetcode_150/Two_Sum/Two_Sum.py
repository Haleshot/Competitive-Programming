# Neetcode:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Step 1 - Brutest of forces
        # if len(nums) == 2:
        #     return [0, 1]
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             if nums.index(nums[i]) == nums.index(nums[j]):
        #                 return [nums.index(nums[i]), nums.index(nums[j], i + 1, len(nums))]
        #             return [nums.index(nums[i]), nums.index(nums[j])]                    

        # # Step 2
        seenMap = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seenMap:
                return [seenMap[remain], i]
            seenMap[nums[i]] = i
        return nums
            

# Leetcode:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Step 1 - Brutest of forces
        # if len(nums) == 2:
        #     return [0, 1]
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             if nums.index(nums[i]) == nums.index(nums[j]):
        #                 return [nums.index(nums[i]), nums.index(nums[j], i + 1, len(nums))]
        #             return [nums.index(nums[i]), nums.index(nums[j])]   

        # # Step 2
        seenMap = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seenMap:
                return [seenMap[remain], i]
            seenMap[nums[i]] = i
        return []
