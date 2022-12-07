# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
# where each new node has its value set to the value of its corresponding original node. 
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that 
# the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

#     val: an integer representing Node.val
#     random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

# Your code will only be given the head of the original linked list.

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# need to do two passes
# first pass creates a deep copy of the nodes, don't link the nodes
# map the original node to the new node in a hashmap
# old node : new node
# second pass will link the nodes

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def printList(self):
        while self:
            if self.next:
                print(f"{self.val}->", end="")
            else:
                print(f"{self.val}->NULL", end="")
            self = self.next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # node can be None, so we set an initial value to the map
        nodeMap = {None : None}

        # first pass copies the node and maps it to our hashmap
        # everything in the hashmap is the copy
        curr = head
        while curr:
            copy = Node(curr.val)
            # nodeMap[[7, None, 0]] = [7, None, None]
            nodeMap[curr] = copy
            curr = curr.next

        # second pass creates the links between the nodes
        # both passes will be iterating through the original list
        curr = head
        while curr:
            # fetch the copy from the hashmap and map the links to the originals in the hashmap
            copy = nodeMap[curr]
            copy.next = nodeMap[curr.next]
            copy.random = nodeMap[curr.random]
            curr = curr.next

        # nodeMap[head] is the head of the copied list since everything in the hashmap is a copy
        return nodeMap[head]

obj = Solution()
l = Node(7,None, None)
l.next = Node(13, None, l)
l.next.next = Node(11, None, l.next)
l.next.next.next = Node(10, None, l.next.next)
l.next.next.next.next = Node(1, None, l)

copy = obj.copyRandomList(l)
copy.printList()