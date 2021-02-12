package LeetCode.String.Reverse_String;

class HyeonJeong {
    public void reverseString(char[] s) {
        int len = s.length;
        char tmp;
        for (int i = 0; i < len/2; i++) {
            tmp = s[i];
            s[i] = s[len-(i+1)];
            s[len-(i+1)] = tmp;
        }
    }
}
