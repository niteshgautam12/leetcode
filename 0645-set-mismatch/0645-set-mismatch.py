class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        actual_sum = sum(nums)
        actual_sq_sum = sum(x*x for x in nums)

        expected_sum = n * (n + 1) // 2
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6

        
        sum_diff = actual_sum - expected_sum      
        sq_sum_diff = actual_sq_sum - expected_sq_sum 

        
        sum_plus = sq_sum_diff // sum_diff        

        duplicate = (sum_diff + sum_plus) // 2
        missing = duplicate - sum_diff

        return [duplicate, missing]
