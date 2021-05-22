class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        nlist = []
        while head != None:
            nlist += [head.val]
            head = head.next

        for i in range((n-m)//2+1):
            num = nlist[m-1+i]
            nlist[m-1+i] = nlist[n-1-i]
            nlist[n-1-i] = num

        result = 0
        for n in nlist:
            if result != 0:
                tmp.next = ListNode(n)
                tmp = tmp.next
            else:
                result = ListNode(n)
                tmp = result
        return result
