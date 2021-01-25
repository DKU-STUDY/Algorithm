'''
https://leetcode.com/problems/add-two-numbers/
Linked_List 문제
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = ''
        while l1 != None:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2 != None:
            num2 = str(l2.val) + num2
            l2 = l2.next

        ret = list(str(int(num1) + int(num2)))
        tmp = None
        for num in ret:
            curNode = ListNode(num, tmp)
            tmp = curNode
        return curNode

'''
'''