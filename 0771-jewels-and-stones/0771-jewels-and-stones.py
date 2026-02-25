class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        y = list(stones)
        count = 0
        for i in range(0,len(stones)):
            if y[i] in jewels:
                count += 1
        return count
