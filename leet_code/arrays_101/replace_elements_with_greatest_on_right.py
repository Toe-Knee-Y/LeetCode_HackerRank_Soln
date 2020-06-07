from typing import *


def replace_elements(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i] = -1
        else:
            arr[i] = max(arr[i + 1:])
    return arr
