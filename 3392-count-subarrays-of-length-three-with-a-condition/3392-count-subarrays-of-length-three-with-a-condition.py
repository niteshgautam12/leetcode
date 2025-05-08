class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        count = 0
        for i in range (0,len(nums)-2):
            if nums[i] + nums[i+2] == nums[i+1]/2.0:
                count += 1
        return count


        