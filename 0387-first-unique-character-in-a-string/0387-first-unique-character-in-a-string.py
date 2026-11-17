class Solution:
    def firstUniqChar(self, s: str) -> int:
        k = dict.fromkeys(s)
        for key in  (k):
            if s.count(key) == 1 :
                return s.index(key)
 
        return -1