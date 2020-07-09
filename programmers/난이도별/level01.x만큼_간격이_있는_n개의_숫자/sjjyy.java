package 난이도별.level01.x만큼_간격이_있는_n개의_숫자;

import java.util.Arrays;

public class sjjyy {
    public static long[] solution(int x, int n)
    {

        long tmp = x;
        long[] answer = new long[n];

        for(int i = 0 ; i < n ; i++)
            answer[i] = tmp * (i + 1);

        return answer;
    }

    public static void main(String [] args)
    {
        System.out.println(Arrays.toString(solution(2, 5))); // [2, 4, 6, 8, 10]
        System.out.println(Arrays.toString(solution(4, 3))); // [4, 8, 12]
        System.out.println(Arrays.toString(solution(-4, 2))); // [-4, -8]
    }
}
