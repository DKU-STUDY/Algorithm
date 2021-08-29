# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # 엣지처리
    if not head:
        return head

    # 길이
    last = head
    LEN = 1
    while last.next:
        last = last.next
        LEN += 1
    # k계산
    k = k % LEN

    # 예외케이스
    if k == 0:
        return head
    cur = head
    for _ in range(LEN - k - 1):
        cur = cur.next
    dummy_head = cur.next
    # cur은 마지막 노드이다.
    cur.next = None
    last.next = head
    return dummy_head