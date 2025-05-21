class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new =[]
        y = list(s)
        # for i in range (len(y)):
        #     if y[i] not in new:
        #         new.append(y[i])
                
        # if len(new) == len(y):
        #     return False
        # else:
        #     return True
        if y[0] != y[-1]:
            return True
        else :
            return False




        