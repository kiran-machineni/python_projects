from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        sum_diagonal = []
        mat_len = len(mat)
        for i in range(mat_len):
            for j in range(mat_len):
                if i == j:
                    sum_diagonal.append(mat[i][j])
                if i + j == mat_len - 1 and i != j:
                    sum_diagonal.append(mat[i][j])
        return sum(sum_diagonal)


my_sol = Solution()

# print(my_sol.diagonalSum([[1, 2, 3],
#                           [4, 5, 6],
#                           [7, 8, 9]]))

print(my_sol.diagonalSum([[1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1]]))

# print(my_sol.diagonalSum([[5]]))
