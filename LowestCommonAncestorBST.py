# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
# between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


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
    def lowestCommonAncestor(self, root: 'TreeNode', p, q) -> int:
        curr = root
        
        while curr:
            # travel down the left tree if p and q are lower than our root
            if p < curr.val and q < curr.val:
                curr = curr.left
            # travel down right tree if p and q are greater than our root
            elif p > curr.val and q > curr.val:
                curr = curr.right
            # in any other case, we would return curr and don't need to traverse any further
            else:
                return curr

obj = Solution()
root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))

print(obj.lowestCommonAncestor(root, 2, 8).val)
print(obj.lowestCommonAncestor(root, 2, 4).val)
print(obj.lowestCommonAncestor(root, 7, 9).val)
print(obj.lowestCommonAncestor(root, 0, 5).val)