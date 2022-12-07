""" Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only. """

def lengthOfLastWord(s: str) -> int:
    length = 0
    # we just need the last word, so we can work backwards
    for c in s[::-1]:
        if c != " ":
            length += 1
        else:
            if length > 0:
                return length

    return length

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))