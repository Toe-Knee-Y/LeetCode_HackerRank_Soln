from typing import *

"""Problem link
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


def minimumBribes(q):
    total_bribes = 0
    for i in range(len(q)):
        original_position = q[i]
        current_position = i + 1

        # Check is the person has bribed more than 2 times
        if original_position - current_position > 2:
            print("Too chaotic")
            return

        # Check the number of people who has bribed the person
        for j in range(max(0, original_position - 2), current_position - 1):
            if q[j] > original_position:
                total_bribes += 1

    print(total_bribes)