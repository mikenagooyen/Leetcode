# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""

    # the first string could be the longest or the shortest, it doesn't matter
    # loop will return prefix if we find a character not common
    for i in range(len(strs[0])):
        for s in strs:
            # check the first string at index i
            # compare the current s string to strs[0]
            # i can go out of bound depending on the string, so check for out of bounds with len(s)
            if i==len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]

    return prefix

arr = ["flower","florist","flight"]
print(longestCommonPrefix(arr))