package 난이도별.level01.정수_내림차순으로_배치하기;

import java.util.Arrays;

public class sjjyy
{
    public static long solution(long n)
    {
        char[] arr = Long.toString(n).toCharArray();

        Arrays.sort(arr);

        StringBuilder stringBuilder = new StringBuilder();

        for (char i : arr)
        {
            stringBuilder.append(i);
        }

        stringBuilder.reverse();

        return Long.parseLong(stringBuilder.toString());
    }

    public static void main(String[] args)
    {
        System.out.println(solution(98023214)); // 98432210
    }
}
