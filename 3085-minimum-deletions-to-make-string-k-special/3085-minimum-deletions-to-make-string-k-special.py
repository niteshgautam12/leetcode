from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        prefix_sum = [0] * (n + 1)
        
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + freq[i]
        
        res = float('inf')
        
        for i in range(n):
            
            max_allowed = freq[i] + k
            
            j = i
            while j < n and freq[j] <= max_allowed:
                j += 1
            
            deletions = prefix_sum[i]  
            for x in range(j, n):
                deletions += freq[x] - max_allowed
            res = min(res, deletions)
        
        return res
