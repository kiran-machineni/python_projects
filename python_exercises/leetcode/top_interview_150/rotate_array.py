# https://leetcode.com/problems/rotate-array/description/
'''
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.
'''
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        return nums


my_sol = Solution()
print(my_sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))
