# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # 1, 2, 2, 2, 5, 5, 5, 8
    # 1: 1, 2: 3, 5: 3, 8
    # 1: 4, 3: 2, 4: 5

    # first we create a hashmap to calculate the number of times
    # each element appear
    hashmap = {}
    for number in A:
        if number not in hashmap:
            hashmap[number] = 1
        else:
            hashmap[number] += 1

    result = 0
    for key in hashmap:
        frequency = hashmap[key]  # number of times the element has appeared
        diff_with_0 = frequency - 0
        diff_with_key = abs(frequency - key)
        # we take the min diff thats either close to 0 or to the number
        # meaning we are calculating if it takes longer to get to the number
        # or to remove the number completely
        diff = min(diff_with_0, diff_with_key)

        result += diff

    return result
print(solution([1, 2, 2]))