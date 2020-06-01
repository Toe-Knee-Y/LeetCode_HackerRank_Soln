import math
import os
import random
import re
import sys

"""Problem Link:
    https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    final_steps = 0
    current_index = 0
    # we want to jump as far as we can each time
    while current_index != len(c) - 1:
        if current_index + 1 == len(c) - 1 or current_index + 2 == len(c) - 1:
            return final_steps + 1

        if c[current_index + 2] == 0:
            current_index += 2
        else:
            current_index += 1

        final_steps += 1
