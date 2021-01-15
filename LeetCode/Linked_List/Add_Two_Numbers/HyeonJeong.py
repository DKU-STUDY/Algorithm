class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nlist = []
        len = 0
        while 1:
            if l1 == None and l2 == None:
                break
            if l1 != None and l2 != None:
                nlist += [l1.val + l2.val]
                l1 = l1.next
                l2 = l2.next
            elif l1 == None:
                nlist += [l2.val]
                l2 = l2.next
            else: # l2 == None
                nlist += [l1.val]
                l1 = l1.next
            len += 1

        for i, n in enumerate(nlist):
        # 각 노드에 한 자리 수만 들어갈 수 있게 리스트를 수정
            if n > 9:
                if i != len-1:
                    nlist[i+1] += nlist[i]//10
                    nlist[i] = n%10

                else:
                    nlist.append(n//10)
                    nlist[i] = n%10

        answer = None
        for n in nlist:
            if answer != None:
                tmp.next = ListNode(n)
                tmp = tmp.next
            else:
                answer = ListNode(n)
                tmp = answer
        return answer
