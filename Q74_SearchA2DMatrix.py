class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        i = 0
        j = len(matrix[0])-1
        while (j >= 0) and (i < len(matrix)):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i+=1
            else:
                j-=1
        return False