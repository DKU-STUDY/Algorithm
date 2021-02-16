package Palindrome_Linked_List;

import java.util.ArrayList;

class HyeonJeong {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null)
            return true;
        int len = 0;
        ArrayList list = new ArrayList();
        while (head != null) {
            list.add(head.val);
            head = head.next;
            len++;
        }
        for (int i = 0; i < len/2; i++) {
            if ((int)list.get(i) != (int)list.get(len-(i+1))) {
                return false;
            }
        }
        return true;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val;}
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
