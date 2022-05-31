def solution(D, X):
    # write your code in Python 3.6
    result = 1
    current_min = D[0] # 0 to start since we know all element is between 1 and 100.....
    current_max = D[0]

    for i in range(1, len(D)):
        curr = D[i]
        if abs(curr - current_min) > X or abs(curr - current_max) > X:
            result += 1
            current_min = curr
            current_max = curr

        current_min = min(current_min, curr)
        current_max = max(current_max, curr)

    # keep to keep track of min
    return result 