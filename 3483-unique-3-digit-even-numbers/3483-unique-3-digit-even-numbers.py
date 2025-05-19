
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """


        new =set()
        for i in range (len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    knew = []
                    if i != j and j != k and k!=i :
                        knew.append(digits[i])
                        knew.append(digits[j])
                        knew.append(digits[k])
                        result = int("".join(map(str, knew)))
                        
                        if result % 2 == 0 and len(str(result)) == 3 :
                    
                            new.add(result)
        return len(new)



        