from typing import Optional
# Definition for singly-linked list.


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


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    mergedList = ListNode()
    tail = mergedList # last node

    # iterate through both lists and check which we need to add to the new merged list
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # if either list 1 or list 2 is still not empty, attach the rest of the list to the end of the node
    # tail.next = list1 or list2 also viable in python
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return mergedList.next # list has default value of 0, so we send the next pointer for the real result


l1, l1.next, l1.next.next = ListNode(1), ListNode(2), ListNode(4)
l2, l2.next, l2.next.next = ListNode(1), ListNode(3), ListNode(4)

merged = mergeTwoLists(l1, l2)

merged.printList(merged)
