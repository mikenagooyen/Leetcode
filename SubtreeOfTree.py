# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# traverse root until we find a value where root.val = subroot.val, and then compare root to the subroot

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subroot is null, then the tree is a subroot of itself as stated
        if not subRoot:
            return True
        # if the root is null, then the subroot can not be a subtree of null
        if not root:
            return False
        # check if the trees are the same at root
        if self.isSameTree(root, subRoot):
            return True
        # recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

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
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subroot = TreeNode(4, TreeNode(1), TreeNode(2))
print(obj.isSubtree(root, subroot))
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0), None)), TreeNode(5))
subroot = TreeNode(4, TreeNode(1), TreeNode(2))
print(obj.isSubtree(root, subroot))