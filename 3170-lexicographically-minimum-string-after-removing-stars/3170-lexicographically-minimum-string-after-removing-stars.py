import heapq
from collections import defaultdict, deque

class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        pq = []  
        index_map = defaultdict(deque)  
        keep = [True] * n  

        for i in range(n):
            if s[i] == '*':
                
                smallest = heapq.heappop(pq)
                idx = index_map[smallest].pop()
                keep[i] = False      
                keep[idx] = False    
            else:
                heapq.heappush(pq, s[i])
                index_map[s[i]].append(i)

        return ''.join(s[i] for i in range(n) if keep[i])
