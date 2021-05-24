# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        for list in lists:
            while list:
                l.append(list.val)
                list = list.next
        l.sort()
        
        root = cur = ListNode(None)
        
        for val in l:
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        
        return root.next