class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 0
        l = list(word)
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                count += 1

        return count + 1


        