
# Given the head of a singly linked list, reverse the list, and return the reversed list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def printList(self):
        while self:
            if self.next:
                print(f"{self.val}->", end="")
            else:
                print(f"{self.val}->NULL", end="")
            self = self.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        # walk through the linked list and reverse their next pointer to the previous
        while curr:
            # store the next link
            temp = curr.next
            # next pointer now points at the previous node
            curr.next = prev
            # prev is now the current node
            prev = curr
            # current node traverses along the list
            curr = temp
        return prev


obj = Solution()
l, l.next,l.next.next,l.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
l = obj.reverseList(l)
l.printList(l)