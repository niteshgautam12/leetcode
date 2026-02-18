class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        h = list(bin(n))
        count = 0 
        for i in range(2,len(h) -1):
            if h[i] == h[i+1]:
                count += 1

        if count > 0 :
            return False
        return True