# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# we don't need to actually change the string, just count the length of the substring
# find a substring and then make a frequency map of that
# length - freq[c] = number of characters we need to replace in the particular substring <= k
# as long as length - freq[c] <= k, window is valid since those are the minimum # of chars to replace
# expand the window until ^ is valid

# slight optimization is to update maxFreq in a single variable instead of looking through hashmap every time for maxFreq
# maxFreq = max(maxFreq, char_map[s[right]])

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        char_map = {}

        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            # keep updating window length and check for valid window
            while (right - left + 1) - max(char_map.values()) > k: # max(char_map.values()) is O(26*n)
                char_map[s[left]] -= 1
                left += 1
            res = max(res, (right - left + 1))

        return res

str = "ABAB"
s = Solution()
print(s.characterReplacement(str, 2))
str = "AABABBA"
print(s.characterReplacement(str, 1))