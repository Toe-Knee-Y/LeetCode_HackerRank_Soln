from typing import *


def sortArrayByParity(A: List[int]) -> List[int]:
    """ How this algorithm works is we have pointers to start and end of the list"""
    # Traverse from front and back of the list
    i = 0
    j = len(A) - 1

    while i < j:
        # if A[i] is even, we are good because we are already at the front of the list for even numbers
        if A[i] % 2 == 0:
            i += 1
        else:
            # that means A[i] is a odd number
            # if A[i] is odd, we swap with values at index j, and we decrease j value by 1 cuz the value
            # is in the right place
            A[i], A[j] = A[j], A[i]
            j -= 1
    return A
