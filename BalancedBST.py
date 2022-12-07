# Given a binary tree, determine if it is height-balanced.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of >every< node never differs by more than one.

# Input: root = [3,9,20,null,null,15,7]
# Output: true

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(f"{' ' * 4 * level} ->  {node.val}")
        printTree(node.left, level + 1)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            # balance will check if left and right subtrees are balanced as well as the difference in heights
            balance = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

            return [balance, 1 + max(left[1], right[1])]

        return dfs(root)[0]

obj = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(obj.isBalanced(root))