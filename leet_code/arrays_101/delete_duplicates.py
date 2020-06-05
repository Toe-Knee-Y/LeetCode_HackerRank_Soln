from typing import *


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    else:
        # This guarantees that we have 2 or more elements in our list
        result = len(nums)
        i = 0

        while i < result - 1:
            if nums[i] == nums[i + 1]:
                # When we have a duplicate num, we shift everything
                for j in range(i, result - 1):
                    nums[j] = nums[j + 1]
                result -= 1
            else:
                i += 1
        return result


if __name__ == "__main__":
    a = [1, 1, 2]
    print(remove_duplicates(a))
    print(a)
