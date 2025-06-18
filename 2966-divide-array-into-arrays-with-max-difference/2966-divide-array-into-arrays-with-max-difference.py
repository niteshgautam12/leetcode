class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        if n % 3 != 0:
            return []

        result = []
        for i in range(0, n, 3):
            group = nums[i:i+3]
            if group[-1] - group[0] <= k:
                result.append(group)
            else:
                return []

        return result
