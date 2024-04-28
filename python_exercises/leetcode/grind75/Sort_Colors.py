from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_dict = {0: 0, 1: 0, 2: 0}
        for i in nums:
            if i == 0:
                nums_dict[i] += 1
            elif i == 1:
                nums_dict[i] += 1
            elif i == 2:
                nums_dict[i] += 1
        nums.clear()
        for key, value in nums_dict.items():
            for _ in range(value):
                nums.append(key)
        return nums


my_sol = Solution()
print(my_sol.sortColors([2, 0, 2, 1, 1, 0]))
