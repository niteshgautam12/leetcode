class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = [] 
        for i in range (len(nums)):
            j = (i + nums[i]+len(nums))%len(nums)
            new.append(nums[j])
        return new