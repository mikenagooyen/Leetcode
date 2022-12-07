# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# in a BST, the smallest elements are all on the left side
# by definition all values are inorder: left, val, right
# for an O(n) solution, we can do inorder traversal and add the a list and then get kth smallest element from there

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list = []

        def dfs(node):
            if node:
                dfs(node.left)
                list.append(node.val)
                dfs(node.right)
        dfs(root)

        # it is 1-indexed, so subtract one from the index
        return list[k - 1]

obj = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(obj.kthSmallest(root, 1))
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6))
print(obj.kthSmallest(root, 3))