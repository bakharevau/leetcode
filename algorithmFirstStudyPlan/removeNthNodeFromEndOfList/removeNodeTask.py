# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        while head is not None:
            lst.append(head)
            head = head.next
        size = len(lst)

        if lst[size - n].next is not None and size - n > 0:
            lst[size - n - 1].next = lst[size - n].next
        else:
            lst[size - n - 1].next = None
        lst.pop(size - n)
        if len(lst):
            return lst[0]
        else:
            return None