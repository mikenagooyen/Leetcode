# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Input: ["lint", "code", "love", "you"]
# Output: ["lint", "code", "love", "you"]
# Explanation: One possible encode method is: "lint:;code:;love:;you"

# The input can have any character, need to figure out a delimiter
# Delimiter can be length of the word + a character: 4#, 5;, 2!, etc.

class Solution:
    def encode(self, strs: str) -> str:
        res = ""
        # we get a list of strings as input and return 1 string
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> str:
        res, i = [], 0

        while i < len(s):
            j = i
            # look for our length and delimiter
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # from j + 1, which is char after #
            res.append(s[(j + 1) : (j + 1 + length)])
            # move to end of the word to start next word
            i = j + 1 + length

        return res

obj = Solution()
input = ["lint", "code", "love", "you"]
print(obj.decode(obj.encode(input)))