package 난이도별.level01.예산;

import java.util.Arrays;

public class sjjyy {
    public static int solution(int[] d, int budget)
    {
        int answer = 0;
        int a = 0;
        int len = d.length;
        Arrays.sort(d);

        for (int i = 0; i < len; i++)
        {
            a += d[i];

            if (a > budget) // 신청 금액이 예산보다 커짐
            {
                answer = i; // 커지기 직전 개수
                return answer;
            }
        }

        if (a <= budget) // 예산이 남거나 딱 맞음
            answer = len;

        return answer;
    }

    public static  int solution2(int[] d, int budget)
    {
        int answer = 0;
        Arrays.sort(d);

        for (int i : d) {
            budget -= i;

            if (budget < 0)
                break;

            answer++;
        }

        return answer;
    }

    public static void main(String[] args)
    {
        int[] d1 = {1,3,2,5,4};
        int[] d2 = {2,2,3,3};
        System.out.println(solution(d1, 9)); // 3
        System.out.println(solution(d2, 10)); // 4

        System.out.println(solution2(d1, 9)); // 3
        System.out.println(solution2(d2, 10)); // 4
    }
}
