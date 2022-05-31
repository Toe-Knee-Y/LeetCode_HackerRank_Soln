def isValid(s: str) -> bool:
    # need to keep track of the order of the parentheses
    order = []
    index = -1
    match = {"(": ")", "[": "]", "{": "}"}

    # first in last out, so this will be a queue
    result = 0
    for i in range(len(s)):
        if s[i] in match:
            order.append(s[i])
            index += 1
            result += 1
        else:
            if result == 0:
                return False
            else:
                if match[order[index]] == s[i]:
                    result -= 1
                    order = order[:-1]
                    index -= 1
                else:
                    return False
    return result == 0

if __name__ == "__main__":
    print(isValid("()[]{}"))