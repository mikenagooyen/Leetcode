# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:

#     -1: Your guess is higher than the number I picked (i.e. num > pick).
#     1: Your guess is lower than the number I picked (i.e. num < pick).
#     0: your guess is equal to the number I picked (i.e. num == pick).

# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
import random

class Solution:
    def __init__(self, num: int):
        self.picked = random.randint(1, num)
        
    def guess(self, num: int) -> int:
        if num > self.picked:
            return -1
        elif num < self.picked:
            return 1

        return 0

    def guessNumber(self, num: int) -> int:
        left = 1
        right = num

        while True:
            mid = (left + right) // 2
            res = self.guess(mid)
            if res > 0:
                left = mid + 1
            elif res < 0:
                right = mid - 1
            else:
                return mid


s = Solution(10)
print(s.guessNumber(10))

#while guessed is False: