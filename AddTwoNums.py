# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# since the linked list represents us adding from right to left as left to right, don't need to overcomplicate
# what to do about carry digits? modulus
# if 11 // 10 = 1 which is the carry digit
# sum % 10 will give us the sum without carry
# loop through each number

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printList(self):
        while self:
            if self.next:
                print(f"{self.val}->", end="")
            else:
                print(f"{self.val}->NULL", end="")
            self = self.next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    sumNode = ListNode()
    curr = sumNode # this is for walking through the sumNode, so when we return, we return the head sumNode
    # curr is just a pointer, sumNode is what we are returning
    carry = 0

    # iterate through the entirety of both lists
    # the carry remainder can occur at last digit
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # carry will always be either 0 or 1
        sum = val1 + val2 + carry
        sum = sum % 10
        carry = sum // 10
        curr.next = ListNode(sum)

        l1 = l1.next if l1.next else None
        l2 = l2.next if l2.next else None
        curr = curr.next

    return sumNode.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
result = addTwoNumbers(l1, l2)
result.printList()