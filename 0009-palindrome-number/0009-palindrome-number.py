class Solution(object):
    def isPalindrome(self, x):
        temp = x
        if x<0:
            return False
        reverse = 0
        while x>0:
            digit = x %10
            reverse = reverse*10 + digit
            x = x//10
        if temp == reverse:
            return True
        return False
        
        