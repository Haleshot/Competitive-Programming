class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answers = []
        # Step 1
        leftptr = 1
        for i in range(len(nums)):
            answers.append(leftptr)
            leftptr *= nums[i]

        rightptr = 1
        for i in range(len(nums) - 1, -1, -1):
            answers[i] *= rightptr
            rightptr *= nums[i]
        return answers

        # # Step 2
        # bef = [1] * len(nums)
        # aft = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     bef[i] = bef[i - 1] * nums[i - 1]

        # for i in range(len(nums) - 2, -1, -1):
        #     aft[i] = aft[i + 1] * nums[i + 1]
        # return [bef[i] * aft[i] for i in range(len(nums))]
