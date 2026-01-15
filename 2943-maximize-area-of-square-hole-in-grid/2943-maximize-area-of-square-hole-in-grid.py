class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def max_gap(bars):
            bars.sort()
            max_consecutive = 1
            curr = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                    max_consecutive = max(max_consecutive, curr)
                else:
                    curr = 1
            
            return max_consecutive + 1
        
        max_h = max_gap(hBars)
        max_v = max_gap(vBars)
        
        side = min(max_h, max_v)
        return side * side
