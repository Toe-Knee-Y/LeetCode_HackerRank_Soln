from typing import *


def valid_mountain_array(A: List[int]) -> bool:
    ascending = True

    if len(A) < 3:
        return False
    else:
        for i in range(len(A) - 1):
            if ascending:
                if A[i + 1] == A[i]:
                    return False
                elif A[i + 1] < A[i]:
                    if i == 0:
                        return False
                    else:
                        ascending = False
            else:
                # now we are descending
                if A[i + 1] >= A[i]:
                    return False
        return not ascending
