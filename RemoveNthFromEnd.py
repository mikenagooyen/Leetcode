# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# we can iterate once to find the end of the list length and then do another loop to remove the node
# use two pointers, left pointer is at the beginning, right pointer is n positions away
# once right ptr is NULL, left is at the node where we want to be so we would remove the next node

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def printList(self):
        while self:
            if self.next:
                print(f"{self.val}->", end="")
            else:
                print(f"{self.val}->NULL", end="")
            self = self.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode(0, head)
        left = curr
        right = head

        # move right pointer n positions from the left
        while n > 0 and right:
            right = right.next
            n -= 1

        # iterate until right is NULL
        while right:
            left = left.next
            right = right.next
            
        # delete the node by pointing it to the next node after deleted
        left.next = left.next.next

        return curr.next


s = Solution()
l, l.next,l.next.next,l.next.next.next,l.next.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
l = s.removeNthFromEnd(l, 2)
l.printList()