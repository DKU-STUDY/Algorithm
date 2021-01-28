package LeetCode.Greedy.Assign_Cookies;

import java.util.Arrays;

class HyeonJeong {
    public int findContentChildren(int[] g, int[] s) {
        int count = 0, g_len = g.length, s_len = s.length, start = g_len-1;
        if (s_len == 0) {
            return count;
        }
        Arrays.sort(g);
        Arrays.sort(s);
        if (s[s_len-1] < g[g_len-1]) {
            for (int i = g_len-1; i > -1 ; i--) {
                if (g[i] <= s[s_len-1]) {
                    start = i;
                    break;
                }
            }
        }
        System.out.println(start);
        System.out.println(s_len-(1));
        int c = 0; // s 배열에서 사용될 수 있는 최대 값의 인덱스를 가리키기 위해 사용
        for (int i = start; i > -1; i--) {
            if (s_len == c) {
                break;
            }
            if (g[i] <= s[s_len-(1+c)]) {
                count++;
                c++;
            }
        }
        return count;
    }
}
