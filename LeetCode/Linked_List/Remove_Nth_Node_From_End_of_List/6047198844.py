# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        removed_n = size - n
        cur = head
        prev = None
        for _ in range(removed_n):
            prev, cur = cur, cur.next
        if prev:
            prev.next = cur.next
        else:
            head = head.next
        return head
        