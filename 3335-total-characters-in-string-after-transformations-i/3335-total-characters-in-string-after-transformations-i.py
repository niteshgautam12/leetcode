class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        from collections import Counter

        MOD = 10**9 + 7
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            next_count = [0] * 26
            for i in range(25):  
                next_count[i + 1] += count[i]
            # 'z' becomes 'a' and 'b'
            next_count[0] += count[25]
            next_count[1] += count[25]
            count = next_count
        
        return sum(count) % MOD
