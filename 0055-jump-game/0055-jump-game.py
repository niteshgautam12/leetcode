class Solution(object):
    def canJump(self,nums):
        farthest = 0
        for i, num in enumerate(nums):
            if i > farthest: return False
            farthest = max(farthest, i + num)
        return True