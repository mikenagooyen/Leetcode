# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# We are looking for the first node with no chilren
# If a node has children, then keep going down until there is none

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + rightDepth
        
        if root.right is None:
            return 1 + leftDepth

        return 1 + min(leftDepth, rightDepth)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(17)

r2 = TreeNode(2)
r2.right = TreeNode(3)
r2.right.right = TreeNode(4)
r2.right.right.right = TreeNode(5)
r2.right.right.right.right = TreeNode(6)

s = Solution()
print(s.minDepth(root))
print(s.minDepth(r2))