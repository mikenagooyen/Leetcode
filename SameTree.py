# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# first check is root, if root == root, go down children

from typing import Optional

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both are null
        if not p and not q:
            return True
        # only one is null
        if not p or not q:
            return False
        # check it value is the same
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

obj = Solution()

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(obj.isSameTree(p,q))
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, None, TreeNode(3))
print(obj.isSameTree(p,q))