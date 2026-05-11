class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = ''.join(str(item) for item in nums)
        p = list(map(int,k))
        return p
        