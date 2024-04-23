from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        common_diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != common_diff:
                return False
        return True


my_sol = Solution()
print(my_sol.canMakeArithmeticProgression([1, 2, 4]))

# [3, 5, 1]
# true
#
# [1,2,4]
# false
