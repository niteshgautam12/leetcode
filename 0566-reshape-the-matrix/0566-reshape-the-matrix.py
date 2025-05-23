class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat = [num for row in mat for num in row]
        if len(flat) != r * c:
            return mat
        
        return [flat[i*c:(i+1)*c] for i in range(r)]