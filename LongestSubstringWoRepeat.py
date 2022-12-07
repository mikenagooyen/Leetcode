# Given a string, find the length of the longest substring without repeating characters

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    res = 0
    left = 0
    
    # find the first character that is not a duplicate by adding it to a set
    # when we find a duplicate, remove the original from the set and use the duplicate as part of the new substring

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        res = max((right - left + 1), res)

    return res

s = "abcabcbb"

print(lengthOfLongestSubstring(s))