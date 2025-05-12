class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = set()
        
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or k == i:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0 and num >= 100:
                        result.add(num)
        
        return sorted(result)
