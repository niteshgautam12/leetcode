class Solution(object):
    def missingNumber(self, nums):
        if len(nums) == 1 and nums[0] == 0 :
            return 1

        nums.sort()

        y = nums.count(0)
        for i in range(y,len(nums) ):
            if len(nums) == 1 :
                return 1
            if nums[i] -  i != 0 :
                return i 
            elif nums[-1] != len(nums):
                return len(nums)
        return 0

        

            
        