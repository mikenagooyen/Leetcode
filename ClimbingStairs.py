# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# define subproblem: how many ways to get to step 5 from step 1, 2, 3, 4, 5
# from step 5, only 1 way to land at step 5
# from step 4, only 1 way to land at step 4
# from step 3, there are two ways to step 5 (2 + 1, 1 + 2)
# from step 2, there are three ways to step 5 (2 + 1, 1 + 2, 1 + 1 + 1)
# from step 1, there are 5 ways to step 5
# from step 0 there are 8 ways
# this is the fibonacci sequence
# break it into a decision tree

# for this DP solution, this is O(n) since each subproblem is solved once


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

obj = Solution()
print(obj.climbStairs(4))