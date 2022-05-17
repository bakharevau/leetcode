class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        while head is not None:
            list.append(head)
            head = head.next
        return list[math.ceil(len(list) / 2)]