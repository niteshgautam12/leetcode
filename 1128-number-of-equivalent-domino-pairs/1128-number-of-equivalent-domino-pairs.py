class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count_map = {}
        count = 0
        
        for d in dominoes:
            key = tuple(sorted(d)) 
            if key in count_map:
                count += count_map[key] 
                count_map[key] += 1
            else:
                count_map[key] = 1
                
        return count
