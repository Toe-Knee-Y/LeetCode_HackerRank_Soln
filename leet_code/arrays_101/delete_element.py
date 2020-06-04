from typing import *


def remove_element(nums: List[int], val: int) -> int:
    result = len(nums)
    i = 0

    while i < result:
        if nums[i] == val:
            for j in range(i, len(nums) - 1):
                nums[j] = nums[j + 1]
            result -= 1
        else:
            i += 1

    return result


if __name__ == "__main__":
    a = [3, 2, 2, 3]
    b = (remove_element(a, 3))
    print(b)
    print(a[:b])
