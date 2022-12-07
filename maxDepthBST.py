from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root, height) -> int:
            if not root:
                return height
            return max(self.traverse(root.left, height + 1), self.traverse(root.right, height + 1))
        return traverse(root, 0)
