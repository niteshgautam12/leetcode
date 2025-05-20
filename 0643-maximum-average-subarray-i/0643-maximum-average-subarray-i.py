class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
       
        w_s = sum(nums[:k])
        max_sum = w_s
        for i in range(k, len(nums)):
            w_s += nums[i] - nums[i - k]
            max_sum = max(max_sum, w_s)
        return round(float(max_sum) / k, 5)
