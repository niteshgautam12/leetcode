class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def is_divisible(s, pattern):
            return s == pattern * (len(s) // len(pattern))
        
        min_len = min(len(str1), len(str2))
        result = ""

        for i in range(1, min_len + 1):
            candidate = str1[:i]
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                if is_divisible(str1, candidate) and is_divisible(str2, candidate):
                    result = candidate  
        return result
