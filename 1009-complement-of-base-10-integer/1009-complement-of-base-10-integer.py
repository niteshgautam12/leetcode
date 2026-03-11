class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = bin(n)[2:]
        # print(p)
        dummy = []
        for i in range (len(p)):
            if p[i] == '1' :
                dummy.append(0)
            else :
                dummy.append(1)
        # print(dummy)
        k = "".join(map(str,dummy))
        l = int(k,2)
        return l
        