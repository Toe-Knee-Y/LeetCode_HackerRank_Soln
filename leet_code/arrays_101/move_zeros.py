from typing import *


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    i = 0
    j = len(nums) - 1

    while i < j:
        a = nums[i]
        b = nums[j]

        if a == 0:
            if b != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            # when a != 0
            if b != 0:
                i += 1
            else:
                i += 1
                j -= 1


if __name__ == "__main__" :
    c = [0, 1, 0, 3, 12, 0, 5, 6, 0, 0]
    moveZeroes((c))
    print(c)
