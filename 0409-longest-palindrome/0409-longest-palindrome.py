class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        count = 0
        has_odd = False

        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

       
        for value in freq.values():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1 
                has_odd = True      

        if has_odd:
            count += 1 

        return count
