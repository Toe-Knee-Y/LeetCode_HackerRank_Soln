import math
import os
import random
import re
import sys

'''Question Link: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup'''


# Complete the countingValleys function below.
def counting_valleys(n, s):
    level = 0
    num_valley = 0
    in_valley = False

    for i in range(n):
        if s[i] == 'U':
            level += 1
            if level == 0:
                in_valley = False
        else:
            level -= 1

        if level < 0:
            if not in_valley:
                num_valley += 1
                in_valley = True

    return num_valley


if __name__ == "__main__":
    print(counting_valleys(12, "DDUUDDUDUUUD"))
