class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        product_count = defaultdict(int)
        n = len(nums)
        result = 0
        
        
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        
        for count in product_count.values():
            if count > 1:
                result += (count * (count - 1) // 2) * 8  
        return result
