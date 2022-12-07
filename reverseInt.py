#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        res = 0

        if x < 0:
            neg = True
        x = abs(x)
        while(x):
            res = res * 10 + x % 10
            x //= 10
        if abs(res) >= 2**31 - 1:
            return 0
        return res if not neg else -res

s = Solution()
print(s.reverse(321))
print(s.reverse(-321))
print(s.reverse(123))