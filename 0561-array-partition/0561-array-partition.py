class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        new = [] 
        for i in range (0,len(nums),2):
            munium = min(nums[i],nums[i+1])
            new.append(munium)
        return sum(new)
        