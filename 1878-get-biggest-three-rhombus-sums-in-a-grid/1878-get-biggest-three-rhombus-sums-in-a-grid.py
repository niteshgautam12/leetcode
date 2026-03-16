class Solution:
    def getBiggestThree(self, grid):
        m = len(grid)
        n = len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):

                sums.add(grid[i][j])

                k = 1
                while True:

                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break

                    total = 0

                    # top -> right
                    x, y = i-k, j
                    for t in range(k):
                        total += grid[x+t][y+t]

                    # right -> bottom
                    x, y = i, j+k
                    for t in range(k):
                        total += grid[x+t][y-t]

                    # bottom -> left
                    x, y = i+k, j
                    for t in range(k):
                        total += grid[x-t][y-t]

                    # left -> top
                    x, y = i, j-k
                    for t in range(k):
                        total += grid[x-t][y+t]

                    sums.add(total)

                    k += 1

        return sorted(sums, reverse=True)[:3]