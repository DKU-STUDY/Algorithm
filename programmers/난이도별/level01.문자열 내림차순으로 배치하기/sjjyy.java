package 난이도별.level01.문자열_내림차순으로_배치하기;

import java.util.Arrays;

public class sjjyy
{
    public static String solution(String str)
    {
        char[] c = str.toCharArray();
        Arrays.sort(c);

        StringBuilder upper = new StringBuilder();
        StringBuilder lower = new StringBuilder();

        for (int i = c.length - 1 ; i >= 0 ; i--)
        {
            if (c[i] >= 'a')
                lower.append(c[i]);
            else
                upper.append(c[i]);
        }

        return String.valueOf(lower.append(upper));
    }

    public static String solution2(String str)
    {
        char[] c = str.toCharArray();
        Arrays.sort(c);
        return new StringBuilder(new String(c)).reverse().toString();
    }

    public static void main(String[] args)
    {
        System.out.println(solution("Zbcdefg"));
        System.out.println(solution2("Zbcdefg"));
    }
}
