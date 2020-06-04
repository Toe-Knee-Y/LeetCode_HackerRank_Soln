from typing import List

"""Problem Link:
    https://leetcode.com/problems/two-sum/
"""


def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = {}

    for i in range(len(nums)):
        if nums[i] not in result:
            result[target - nums[i]] = i
        else:
            return [result[nums[i]], i]


