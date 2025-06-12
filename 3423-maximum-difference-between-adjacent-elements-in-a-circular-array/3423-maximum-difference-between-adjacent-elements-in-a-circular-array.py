class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        n = len(nums)
        ans = abs(nums[0] - nums[-1])      
        for i in range(1, n):
            ans = max(ans, abs(nums[i] - nums[i - 1]))
        return ans
