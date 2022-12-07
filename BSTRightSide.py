# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# in other words, view it as if the right nodes are blocking whatever is on the left.
# if a left node exists where it is not blocked by a right node, we have to add that as well to our output
# we can do a breadth first search and do a level traversal on the tree
# if we add in left and right, we can pop the left value from our results
# for each level, we want the right most node

from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            right = None
            # we will only every pop two nodes at a time, and since it is added left to right, queueLength will be either 1 or 2
            # if queueLength is 1, that means no right node is blocking it from our view
            # if queueLength is 2, that means the second node we pop is our right node
            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    right = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right:
                res.append(right.val)

        return res

obj = Solution()
root = TreeNode(1, TreeNode(2, None, TreeNode(5, TreeNode(7), None)), TreeNode(3, None, TreeNode(4)))
print(obj.rightSideView(root))