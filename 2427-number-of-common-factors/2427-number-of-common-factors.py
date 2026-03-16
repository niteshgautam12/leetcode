class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0 

        p = []
        l =[]
        for i in range (1,a):
            if a%i == 0 :
                p.append(i)
        for i in range(1,b):
            if b%i == 0:
                l.append(i)
        c = p + l
        c.sort()
        for i in range (len (c)-1):
            if c[i] == c[i+1]:
                count += 1
        if max(a,b)%min(a,b) == 0:
            count += 1
        return count


        