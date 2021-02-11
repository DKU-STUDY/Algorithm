package LeetCode.Linked_List.Swap_Nodes_in_Pairs;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class HyeonJeong {
    public ListNode swapPairs(ListNode head) {
        ListNode node = head;
        int tmp;
        while (node != null && node.next != null) {
            tmp = node.val;
            node.val = node.next.val;
            node = node.next;
            node.val = tmp;
            node = node.next;
        }
        return head;
    }
}
