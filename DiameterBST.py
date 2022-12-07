# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# start from the bottom and work our way up so make as few calls as possible


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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # python specific, the dfs function won't change res if it were a primitive, so we use list object for a pass by reference
        res = [0]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)  # left and right are tree height
            right = dfs(root.right)
            # diameter of current node is the left height + right height
            res[0] = max(res[0], left + right) 
            return 1 + max(left, right)  # return height of the tree

        dfs(root)
        # each node is visited only once so this is O(n)
        return res[0]


obj = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(obj.diameterOfBinaryTree(root))
