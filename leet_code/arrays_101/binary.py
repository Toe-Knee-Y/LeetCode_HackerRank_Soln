

def hasAllCodes(s: str, k: int) -> bool:
    # generate the list of substrings
    hashmap = {}
    for i in range(len(s) - (k - 1)):
        substring = s[i:i + k]
        if substring not in hashmap:
            hashmap[substring] = 1
    print(hashmap)
    for i in range(2 ** k):
        binary = f"{i:b}"
        if len(binary) != k:
            binary = "0" * (k - len(binary)) + binary
        if binary not in s:
            return False
        else:
            print(binary)

    return True


hasAllCodes("00110110", 2)