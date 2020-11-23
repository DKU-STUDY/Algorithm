package 난이도별.level01.자연수_뒤집어_배열로_만들기;

import java.util.Arrays;

public class sjjyy
{
    public static int[] solution(long n)
    {
        String ans = String.valueOf(n);
        int len = ans.length();
        int [] answer = new int[len];

        for (int i = 0 ; i < len ; i++)
            answer[i] = Integer.parseInt(String.valueOf(ans.charAt(len - i -1)));

        return answer;
    }

    public static void main(String[] args)
    {
        System.out.println(Arrays.toString(solution(12345)));
        System.out.println(Arrays.toString(solution(19)));
    }
}
