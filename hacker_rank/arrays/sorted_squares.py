from typing import *


def sorted_squares(a: List[int]) -> List[int]:
    result = []
    current_min = a[0]
    current_max = 0

    for number in a:
        number_squared = number * number
        if number_squared >= current_max:
            result.append(number_squared)
            current_max = number_squared
        elif number_squared <= current_min:
            result.insert(0, number_squared)
            current_min = number_squared
        else:
            inserted = False
            for i in range(len(result)):
                if result[i] > number_squared and not inserted:
                    result.insert(i, number_squared)
                    inserted = True
            if not inserted:
                result.append(number_squared)
    return result


if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))
