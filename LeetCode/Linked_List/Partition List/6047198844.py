# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = dummy_first = ListNode(0)
        second = dummy_second = ListNode(0)

        while head:
            if head.val < x:
                dummy_first.next = ListNode(head.val)
                dummy_first = dummy_first.next
            else:
                dummy_second.next = ListNode(head.val)
                dummy_second = dummy_second.next
            head = head.next

        dummy_first.next = second.next
        return first.next