class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for p in range(1, n):
            l = n - p
            if '0' not in str(p) and '0' not in str(l):
                return [p, l]



        