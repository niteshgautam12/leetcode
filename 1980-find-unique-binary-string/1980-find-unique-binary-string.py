class Solution(object):
    def findDifferentBinaryString(self, nums):
        nums.sort()
        n = len(nums)

        for i in range(2**n):
            b = bin(i)[2:].zfill(n)
            if b not in nums:
                return b