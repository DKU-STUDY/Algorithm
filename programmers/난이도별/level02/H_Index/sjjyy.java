package programmers.난이도별.level02.H_Index;

import java.util.Arrays;

public class sjjyy {

    public static int solution(int[] citations) {
        int answer = 0;
        int len = citations.length;



        Arrays.sort(citations);

        for (int i = 0; i < len; i++) {
            int h = len - i;
            answer = Math.max(answer, Math.min(citations[i], h));

             /*
                if ( h <= citations[i]) {
                    answer = h;
                    break;
                }

             */

        }

        return answer;

    }

    public static int solution2(int[] citations) {
        int answer = 0;
        int len = citations.length;



        Arrays.sort(citations);

        for (int i = 0; i < len; i++) {
            int h = len - i;
            answer = Math.max(answer, Math.min(citations[i], h));

             /*
                if ( h <= citations[i]) {
                    answer = h;
                    break;
                }

             */

        }

        return answer;

    }

    public static void main(String[] args) {
        int[] citations = {3, 0, 6, 1, 5};
        System.out.println(solution(citations)); // 3
        System.out.println(solution2(citations)); // 3
    }
    
}
