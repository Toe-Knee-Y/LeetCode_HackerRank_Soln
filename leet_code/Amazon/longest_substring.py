def lengthOfLongestSubstring(s: str) -> int:

    i, j = 0, 0
    current = 0
    longest = 0
    hashtable = {}

    while i < len(s) or j < len(s):
        if i == j:
            j += 1
            return





if __name__ == "__main__":
    print(lengthOfLongestSubstring("abba"))
    print()
