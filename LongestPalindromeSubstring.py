def longestPalindrome(s: str) -> str:
    if not s or len(s) < 1: return ""

    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expandFromMid(s, i, i)
        len2 = expandFromMid(s, i, i+1)
        length = max(len1, len2)
        if length > (end - start):
            start = int(i - ((length-1)//2)) #int casting rounding is inconsistent so use floor //
            end = int(i + (length/2))
            
    return s[start:end + 1]


def expandFromMid(s, left: int, right: int) -> int:
    if not s or left > right: return 0

    while (left >= 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    return right - left - 1

print(longestPalindrome("racecar"))