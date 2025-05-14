class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count0 = s.count('0')
        count1 = s.count('1')
        
        if abs(count0 - count1) > 1:
            return -1
        
        def mismatches(start_char):
            expected = start_char
            mismatch = 0
            for ch in s:
                if ch != expected:
                    mismatch += 1
                expected = '0' if expected == '1' else '1'
            return mismatch // 2
        
        if count0 > count1:
            return mismatches('0')
        elif count1 > count0:
            return mismatches('1')
        else:
            return min(mismatches('0'), mismatches('1'))
