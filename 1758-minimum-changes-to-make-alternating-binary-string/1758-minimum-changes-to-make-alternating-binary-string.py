class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [int(ch) for ch in s]
        count_same = 0  
        count_diff = 0 

        for i in range(len(l) - 1):
            if l[i] == l[i+1]:
                count_same += 1
            else:
                count_diff += 1

        
        pattern1 = 0
        pattern2 = 0
        for i in range(len(l)):
            if l[i] != (i % 2):       
                pattern1 += 1
            if l[i] != ((i + 1) % 2):  
                pattern2 += 1

        return min(pattern1, pattern2)
