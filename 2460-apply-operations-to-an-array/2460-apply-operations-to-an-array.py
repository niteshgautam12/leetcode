class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0  
        
        
        result = []
        zero_count = 0
        
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zero_count += 1
        
        result.extend([0] * zero_count)  
        
        return result
