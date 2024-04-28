from typing import List

import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        left_list = []
        right_list = []
        for i in range(len(nums)):
            left_list[:] = nums[:i]
            right_list[:] = nums[i + 1:]
            product_list.append(math.prod(left_list + right_list))
            left_list = []
            right_list = []
        return product_list


my_sol = Solution()

print(my_sol.productExceptSelf([1, 2, 3, 4]))
# output: [24,12,8,6]


# ======= solution with o(n)=============
from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         left_product = [1] * n
#         right_product = [1] * n
#
#         # Calculate left and right cumulative products
#         for i in range(1, n):
#             left_product[i] = left_product[i - 1] * nums[i - 1]
#         for i in range(n - 2, -1, -1):
#             right_product[i] = right_product[i + 1] * nums[i + 1]
#
#         # Combine left and right products for each element
#         product_list = [left * right for left, right in zip(left_product, right_product)]
#         return product_list
#
# 
# my_sol = Solution()
# print(my_sol.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]


