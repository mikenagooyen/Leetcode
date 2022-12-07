# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # we use an array of a-z as our hashmap
        dict1 = [0] * 26
        # add to count of characters found in string at index of character
        for i in range(len(s1)):
            dict1[ord(s1[i]) - ord('a')] += 1
        
        i, match = 0, len(s1)
        # sliding window through s2
        # if we find a matching letter, we decrement match
        # match = 0 would mean a permutation

        for j in range(len(s2)):
            # check the array at index of the character and see if it exists in array
            if(dict1[ord(s2[j]) - ord('a')] > 0): # found the letter in array which is a match, so we decrement match
                match -= 1
            dict1[ord(s2[j]) - ord('a')] -= 1 # decrement the count at index of character at every pass
            j += 1 # slide window right
            if match == 0: 
                return True
            # once the window is the same size as the length of s1, we can start shifting over the left index and fix the indices that were decremented
            # reset the match value and array counts and keep sliding to the right
            if j - i == len(s1):
                if dict1[ord(s2[i]) - ord('a')] >= 0:
                    match += 1
                dict1[ord(s2[i]) - ord('a')] += 1
                i += 1
        return match == 0


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("ab", "eidboaoo"))