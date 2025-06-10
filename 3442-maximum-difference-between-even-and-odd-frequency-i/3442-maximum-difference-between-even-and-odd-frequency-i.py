from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)

        odds = [v for v in freq.values() if v % 2 == 1]
        evens = [v for v in freq.values() if v % 2 == 0]

        if not odds or not evens:
            return -1

        return max(o - e for o in odds for e in evens)
