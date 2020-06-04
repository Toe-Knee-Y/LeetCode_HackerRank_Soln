from typing import *


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    original_length = len(arr)
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            i += 2
        else:
            i += 1

    for i in range(len(arr) - original_length):
        arr.pop()