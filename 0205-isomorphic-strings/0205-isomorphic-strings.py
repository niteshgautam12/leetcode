class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        mapping_st = {}
        mapping_ts = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

           
            if c1 in mapping_st:
                if mapping_st[c1] != c2:
                    return False
            else:
                mapping_st[c1] = c2

           
            if c2 in mapping_ts:
                if mapping_ts[c2] != c1:
                    return False
            else:
                mapping_ts[c2] = c1

        return True
