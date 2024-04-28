from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    h = {}
    for i, num in enumerate(nums):
        h[num] = i
    for i, num in enumerate(nums):
        desired = target - num
        if desired in h and h[desired] != i:
            return [i, h[desired]]


print(twoSum([2, 2, 4], 6))
