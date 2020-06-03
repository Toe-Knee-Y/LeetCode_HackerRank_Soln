from typing import *


def sortedSquares(A: List[int]) -> List[int]:
    result = []

    for i in range(len(A)):
        squared = A[i] ** 2
        if len(result) == 0:
            result.append(squared)
        else:
            for j in range(len(result)):
                if result[j] > squared:
                    result.insert(j, squared)
    return result


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 3, 10]))
