class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        count = 0 
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
        if count == 0 :
            return False
        else :
            return True