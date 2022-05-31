def solution(S):
    # write your code in Python 3.6
    # first we create a hashmap calculating the frequency of the letter chunks
    if len(S) == 0:
        return 0
    else:
        # we know for sure we have at least 1 char in the string
        previous = S[0]
        hashmap = {0: 1}
        counter = 0
        global_max = 1
        for i in range(1, len(S)):
            curr = S[i]
            if curr == previous:
                hashmap[counter] += 1
            else:
                counter += 1
                hashmap[counter] = 1
            global_max = max(hashmap[counter], global_max)
            previous = curr

        result = 0
        for key in hashmap:
            diff = global_max - hashmap[key]
            result += diff

        return result

print(solution('babaaaaaaa'))