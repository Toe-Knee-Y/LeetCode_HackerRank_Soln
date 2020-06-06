from typing import *


def check_if_exist(arr: List[int]) -> bool:
    for i in range(len(arr)):
        num = arr[i]
        for j in range(i + 1, len(arr)):
            if num * 2 == arr[j] or arr[j] * 2 == num:
                return True
    return False

