class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        
        words.reverse()
        


        
        groups.reverse()
        new = []

        for i in range (len(groups)-1):
            if groups[i] != groups[i+1]:
            
                new.append(words[i])
        new.append(words[-1])
        new.reverse()
                
        return new