from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_arr = []
        for account in accounts:
            wealth_arr.append(sum(account))
        return max(wealth_arr)


my_sol = Solution()

print(my_sol.maximumWealth([[1, 2, 3], [3, 2, 1]]))

# print(my_sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))

# print(my_sol.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
