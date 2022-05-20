# Definition for singly-linked list.
import optional as optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                lst.next = list1
                lst = list1
                list1 = list1.next

            else:
                lst.next = list2
                lst = list2
                list2 = list2.next

        if list1 or list2:
            lst.next = list1 if list1 else list2
        return head.next
