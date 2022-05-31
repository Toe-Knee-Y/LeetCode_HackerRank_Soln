from typing import List

def reverseWords(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        j -= 1
        i += 1

    i = 0
    j = 0

    while i < len(s):
        while  j < len(s) and s[j] != " " :
            j += 1

        for k in range((j - i) // 2):
            s[i + k], s[j - 1 - k] = s[j - 1 - k], s[i + k]

        i = j + 1


print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
