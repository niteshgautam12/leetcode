class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result =[]




        for i in range (len(candies)):
            if candies[i] + extraCandies >= max(candies) :
                result.append(True)
            else :
                result.append(False)
        return result
        