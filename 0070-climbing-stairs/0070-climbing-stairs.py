class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        count1 = 1
        count2 = 2
        for i in range (2,n):
            count1,count2 = count2,count2 +count1
        return count2
                
        