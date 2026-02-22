class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        max_gap = 0
        index = 0
        
        while n > 0:
            if n & 1: 
                if prev != -1:
                    max_gap = max(max_gap, index - prev)
                prev = index
            n >>= 1 
            index += 1
        
        return max_gap