class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        
        diff = [(s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]
        
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        else:
            return False
