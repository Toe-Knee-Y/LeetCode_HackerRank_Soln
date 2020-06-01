"""Problem Link:
    https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""


def repeatedString(s, n):
    positions = []
    num_in_s = 0

    for i in range(len(s)):
        if s[i] == 'a':
            positions.append(i)
            num_in_s += 1

    result = (n // len(s)) * len(positions)
    for i in range((n % len(s))):
        if i in positions:
            result += 1
    return result


if __name__ == "__main__":
    print(repeatedString("aba", 10))
