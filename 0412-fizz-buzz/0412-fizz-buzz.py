class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        new = []
        for i in range(1,n+1):
            if i % 3 == 0 and i%5 != 0 :
                new.append("Fizz")
            elif i%5 == 0 and i%3 != 0 :
                new.append("Buzz")
            elif i%3 == 0 and i%5 == 0 :
                new.append("FizzBuzz")
            else :
                new.append(str(i))
        return new

