# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = cur = ListNode(0)
        cur.next = head
        
        while cur.next and cur.next.next:
            p, q = cur.next, cur.next.next
            cur.next, p.next, q.next = q, q.next, p
            cur = p
            
            
        return root.next
        