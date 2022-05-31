def permutation(letters: str):
    """Output all possible combination of the given letters to the given file"""

    # base case:
    if len(letters) == 1:
        return [letters]
    else:
        result = []
        for index, letter in enumerate(letters):
            rest = letters[:index] + letters[index+1:]
            rest_perm = permutation(rest)
            for i in range(len(rest_perm)):
                rest_perm[i] = letter + rest_perm[i]
            result.extend(rest_perm)

        return result


def _factorial(num) -> int:
    """return the factorial of the given number"""
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


result = permutation("abcd")

for item in result:
    print(item)
