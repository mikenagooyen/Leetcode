# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# preorder = root.val + root.left + root.right
# inorder = root.left + root.val + root.right
# the first value in preorder is the root
# the second value is the beginning of the subtree of the left subtree
# everything to the left of the root in inorder list is the left subtree
# recursive calls using array index splicing

from typing import Optional, List

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # mid is the index of our root node in inorder array
        # that is, everything to the left of mid is the left subtree
        mid = inorder.index(preorder[0])

        # preorder goes from 1 (the root node is at 0), to mid + 1
        # [1:2] will basically just be index[1]
        # inorder goes from 0 to mid
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # preorder goes from mid + 1 til the end
        # inorder goes from mid + 1 til the end
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

obj = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20 ,7]

root = obj.buildTree(preorder, inorder)
printTree(root)