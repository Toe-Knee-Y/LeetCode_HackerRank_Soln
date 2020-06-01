
"""Question link: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup"""
import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_tracker = {}

    result = 0;
    for i in range(n):
        if ar[i] in sock_tracker:
            if sock_tracker[ar[i]] == 1:
                result += 1
                sock_tracker[ar[i]] -= 1
            else:
                sock_tracker[ar[i]] += 1
        else:
            sock_tracker[ar[i]] = 1

    return result
