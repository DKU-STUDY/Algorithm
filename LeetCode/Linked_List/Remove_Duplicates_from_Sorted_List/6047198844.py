# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        
        while cur:
            next_cur = cur
            while next_cur and next_cur.val == cur.val:
                next_cur = next_cur.next
            cur.next = next_cur
            cur = cur.next
            
        return head
        