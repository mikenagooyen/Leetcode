# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# 1 -> 2 -> 3 -> 4 turns into 1 -> 4 -> 2 -> 3

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

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
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # iterate through until we find the end of the list
        # at the end, slow will be where we want to split our list in half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        prev = slow.next = None

        # reverse the second half of the list
        # at the end, right will be None and prev will be pointing towards the beginning of the right half that got reversed
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        # merge the lists here
        left, right = head, prev
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1 
            left, right = temp1, temp2

        return None

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s.reorderList(head)
head.printList(head)