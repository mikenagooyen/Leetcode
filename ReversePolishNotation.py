# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. 

# That means the expression would always evaluate to a result, and there will not be any division by zero operation.

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# keep adding to a stack
# once you find an operator, pop twice and perform the operation, result goes back into the stack
# if no more operations result is the only item in the stack
# order of operands matter for subtraction and division

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operater_set = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token not in operater_set:
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == "+":
                    stack.append(op1 + op2)
                elif token == "-":
                    stack.append(op2 - op1)
                elif token == "*":
                    stack.append(op1 * op2)
                elif token == "/":
                    stack.append(int(op2 / op1))

        return stack[0]

obj = Solution()
print(obj.evalRPN(["2","1","+","3","*"]))
print(obj.evalRPN(["4","13","5","/","+"]))
print(obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))