package LeetCode.Greedy.Assign_Cookies;

import java.util.Arrays;

class HyeonJeong {
    public int findContentChildren(int[] g, int[] s) {
        //아이들이 만족하는 쿠키의 최소 크기가 담긴 g와 쿠키 크기가 담긴 s 배열을 이용해 만족하는 최대 경우를 구하는 문제
        int count = 0, g_len = g.length, s_len = s.length, start = g_len-1;
        // 자주 사용될 두 배열의 길이를 변수에 저장
        // start를 s[s_len-1] >= g[g_len-1]일 경우 사용될 값으로 선언
        if (s_len == 0) { // 줄 수 있는 쿠키 크기가 담긴 값이 없는 경우
            return count;
        }
        Arrays.sort(g);
        Arrays.sort(s);
        for (int i = g_len-1; i > -1 ; i--) {
            if (g[i] <= s[s_len-1]) {
                start = i;
                break;
            }
        }
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
