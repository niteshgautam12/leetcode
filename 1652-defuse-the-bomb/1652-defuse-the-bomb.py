class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        new = []

        if k > 0:
            for i in range(n):
                total = 0
                for j in range(1, k + 1):
                    total += code[(i + j) % n]  
                new.append(total)

        elif k == 0:
            new = [0] * n

        else:  # k < 0
            for i in range(n):
                total = 0
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]  
                new.append(total)

        return new
