def permutation(letters: str, file):
    """Output all possible combination of the given letters to the given file"""

    result = ""
    # one way of constructing the string is by population the list as we move to each letter
    for index, letter in enumerate(letters):
        result += (letter + "\n") * _factorial(len(letters) - 1)

    with open(file, 'w') as f:
        f.write(result)


def _factorial(num) -> int:
    """return the factorial of the given number"""
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


permutation("abcd", "./permutation.txt")