class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        for i in range (len(nums)):
            k = str(nums[i])
            p = len(k)
            if p%2 == 0 :
                count += 1
        return count