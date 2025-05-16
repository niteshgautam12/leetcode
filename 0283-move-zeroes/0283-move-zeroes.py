class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = nums.count(0)
        new = []
        for i in range(len(nums)):
            if nums[i] != 0 :
                new.append(nums[i])
        for j in range(p):
            new.append(0)
        for i in range (len(new)):
            nums[i] = new[i]
        return nums