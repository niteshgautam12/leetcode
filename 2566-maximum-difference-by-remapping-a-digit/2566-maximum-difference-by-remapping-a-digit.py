class Solution:
    def minMaxDifference(self, num: int) -> int:
        k = [int(d) for d in str(num)]  # convert number to digit list
        s = str(num)

       
        for d in s:
            if d != '9':
                max_digit = d
                break
        else:
            max_digit = None  
        
        if max_digit:
            new = [9 if str(x) == max_digit else x for x in k]
        else:
            new = k[:]

        
        for d in s:
            if d != '0':
                min_digit = d
                break
        else:
            min_digit = None  

        if min_digit:
            knew = [0 if str(x) == min_digit else x for x in k]
        else:
            knew = k[:]


        p = int(''.join(map(str, new)))
        q = int(''.join(map(str, knew)))
        return p - q
