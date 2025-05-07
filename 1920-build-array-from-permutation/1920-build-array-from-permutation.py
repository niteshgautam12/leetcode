class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new  = []
        demo = 0

        for i in range (len(nums)):
            if nums[i] == i :
                new.append(i)
            else :
                demo = + nums[i]
                new.append(nums[demo])
        return new

        