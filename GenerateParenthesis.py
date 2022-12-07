# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# we need n open parenthesis and n closed parenthesis
# must start with an open parenthesis up to n parenthesis
# can only add a closed parenthesis if our open paren count is > closed
# only add open paren if open < n

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN, closedN):
            # base case, when our # of paren = n
            if openN == closedN == n:
                res.append("".join(stack))
                return
                
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # pop the character from the stack every time we finish the recursive call
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0,0)

        return res

obj = Solution()
print(obj.generateParenthesis(3))