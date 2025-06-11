class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        rotated = nums[-k:] + nums[:-k]  
        nums[:] = rotated
        return rotated