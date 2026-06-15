class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])

        zeros_row = [False] * m
        zeros_col = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeros_row[row] = True
                    zeros_col[col] = True
        
        for row in range(m):
            for col in range(n):
                if zeros_row[row] or zeros_col[col]:
                    matrix[row][col] = 0