from typing import *


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # When nums 1 is empty, we just copy everything from nums2
    if m == 0:
        for k in range(n):
            nums1[k] = nums2[k]
    else:
        i = 0
        j = 0
        while j != n:
            if nums2[j] <= nums1[i]:
                # insert the element to nums1 and shift everything down ward
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                i += 1
            else:
                i += 1
                # m + j implies that we have iterated all the original elements in nums1
                # hence we need to add values after the original elements
                if i == m + j:
                    nums1[i] = nums2[j]
                    j += 1


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    merge(a , 3, [2, 5, 6], 3)
    print(a)