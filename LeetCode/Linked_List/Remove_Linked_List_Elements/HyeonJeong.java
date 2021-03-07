package Remove_Linked_List_Elements;

class HyeonJeong {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) // 노드 값이 없는 경우
            return null;
        while (head != null && head.val == val) { // 시작 노드의 값을 제거
            head = head.next;
        }
        if (head == null) // 노드 값이 모두 제거되는 경우
            return null;

        ListNode copy = head; // 반환할 링크드 리스트의 시작
        while (head != null) {
            if (head.next != null && head.next.val == val) { // val과 노드의 값이 같은 경우
                head.next = head.next.next;
                continue;
            }
            head = head.next;
        }
        return copy;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val;}
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
