# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = cur = ListNode(0)

        while l1 or l2 or carry:  # l1, l2가 모두 널이면서 carry가 없을때 종료한다.
            val1 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next

            val2 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next

            carry, val = divmod(val1 + val2 + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next

        return res.next
