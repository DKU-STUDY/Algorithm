package LeetCode.String.To_Lower_Case;

class HyeonJeong {
    public String toLowerCase(String str) {
        return str.toLowerCase(); // 문자열을 모두 소문자로 변경시켜 반환

        /*
        StringBuffer sb = new StringBuffer();
        int n;
        for (int i = 0; i < str.length(); i++) {
            n = str.charAt(i);
            if (65 <= n && n <= 90) // 대문자인 경우
                sb.append((char)(n + 32));
            else
                sb.append((char)n);
        }
        String s = new String(sb);
        return s;
         */
    }
}
