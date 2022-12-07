# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")" : "(", "}" : "{", "]": "["}
        
        # add open character to the stack
        # if you find a closing character, check the hashmap and see if it exists
        # pop the open character if stack is not empty and continue
        for c in s:
            if c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

obj = Solution()
print(obj.isValid("()"))
print(obj.isValid("(]"))
print(obj.isValid("([{}])"))