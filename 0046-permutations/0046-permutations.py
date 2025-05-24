import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        combination = list(itertools.permutations(nums))
        return [list(p) for p in combination]
       
        