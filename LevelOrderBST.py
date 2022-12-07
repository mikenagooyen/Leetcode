# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# BFS Problem, use a queue

#Definition for a binary tree node.

from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            level = []
            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level: #make sure level is non empty before we add
                res.append(level)

        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(17)

r2 = TreeNode(1)

r3 = TreeNode()

s = Solution()
print(s.levelOrder(root))
print(s.levelOrder(r2))
print(s.levelOrder(r3))