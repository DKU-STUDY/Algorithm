class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = None
        value = -101 # 정렬된 링크드 리스트의 중복요소 제거에 사용
        while head != None:
            if value < head.val:
                value = head.val
                if result != None:
                    tmp.next = ListNode(value)
                    tmp = tmp.next
                else:
                    result = ListNode(value)
                    tmp = result
            head = head.next
        return result
