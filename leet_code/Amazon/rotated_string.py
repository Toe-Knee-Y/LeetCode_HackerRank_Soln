from typing import List


def rotated_string(lst: List) -> int:
    """The array is in ascending order and it could be rotated,
    we want to find the minimum number of the array

    """

    # we are using the binary search algorithm to determine
    # which half of the array we want to choose each time
    # [1, 2, 3, 4, 5] -> 1
    # [2, 3, 4, 5, 1]
    # [4, 5, 1, 2, 3]
    # [5, 1, 2, 3, 4]

    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return min(lst)
    else:
        mid = len(lst) // 2
        right = lst[-1]

        if lst[mid] > right:
            return rotated_string(lst[mid:])
        else:
            return rotated_string(lst[:mid + 1])

print(rotated_string([4, 5, 7, 8, 3]))