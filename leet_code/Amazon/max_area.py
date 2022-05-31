from typing import List


def maxArea(height: List[int]) -> int:
    front = 0
    back = len(height) - 1
    max_area = 0

    while front < back:
        current_area = min(height[front], height[back]) * (back - front)
        max_area = max(current_area, max_area)

        if height[front] < height[back]:
            front += 1
        else:
            back -= 1

    return max_area

print(maxArea([2,3,4,5,18,17,6]))