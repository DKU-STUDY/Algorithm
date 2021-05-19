# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        root = head
        odd = odd_cur = ListNode(0)
        even = even_cur = ListNode(0)
        
        while head and head.next:
            odd_cur.next, even_cur.next = head, head.next
            odd_cur, even_cur = odd_cur.next, even_cur.next
            head = head.next.next
        
        if head:
            odd_cur.next = head
            odd_cur = odd_cur.next
            even_cur.next = None
        
        odd_cur.next = even.next
        
        return root