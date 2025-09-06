class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        k = abs(x - z)
        n = abs(y - z)
        if min (k,n) == k and k != n:
            return 1
        elif min (k,n) == n and k != n :
            return 2
        else :
            return 0
        