from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # Identify which rows and columns contain zeroes
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Zero out the rows
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0

        # Zero out the columns
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0
        print(matrix)


my_sol = Solution()

# print(my_sol.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# output: [[1,0,1],[0,0,0],[1,0,1]]

print(my_sol.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
