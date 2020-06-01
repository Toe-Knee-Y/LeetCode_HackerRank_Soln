"""Problem Link:
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """

    current_longest = 0
    current_str = ''

    for i in range(len(s)):
        if s[i] not in current_str:
            current_str = current_str + s[i]
        else:
            current_str = current_str[current_str.index(s[i]) + 1:] + s[i]

        if len(current_str) > current_longest:
            current_longest = len(current_str)

    return current_longest
