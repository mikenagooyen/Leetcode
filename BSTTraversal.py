
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], list: List[int]):
        if root:
            self.traverse(root.left,list)
            list.append(root.val)
            self.traverse(root.right,list)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        self.traverse(root, list)
        return list

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []