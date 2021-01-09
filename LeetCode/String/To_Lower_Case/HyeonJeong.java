package LeetCode.String.To_Lower_Case;

class HyeonJeong {
    public String toLowerCase(String str) {
        StringBuffer sb = new StringBuffer();
        int n;
        for (int i = 0; i < str.length(); i++) {
            n = str.charAt(i);
            if (65 <= n && n <= 90)
                sb.append((char)(n + 32));
            else
                sb.append((char)n);
        }
        String s = new String(sb);
        return s;
    }
}