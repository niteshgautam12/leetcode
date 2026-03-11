class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left , right = 0 , len(numbers) -1
        while left < right :
            sum_num = numbers[left] + numbers[right]
            if sum_num == target :
                return (left+1,right+1)
            elif sum_num < target :
                left += 1
            else :
                right -= 1
        return None        