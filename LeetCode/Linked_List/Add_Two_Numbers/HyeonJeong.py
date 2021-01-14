class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nlist = []
        carry = 0
        while 1:
            if l1 == None and l2 == None:
                break
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            add = x + y + carry
            if add > 9:
                carry = add//10
                nlist += [add%10]
            else:
                carry = 0
                nlist += [add]
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        if carry != 0:
            nlist += [carry]
        result = None
        for n in nlist:
            if result != None:
                tmp.next = ListNode(n)
                tmp = tmp.next
            else:
                result = ListNode(n)
                tmp = result
        return result
