package 난이도별.level01.문자열_내_마음대로_정렬하기;

import java.util.Arrays;

public class sjjyy
{
    public static String[] solution(String[] strings, int n)
    {
        int len = strings.length;
        for (int i = 0 ; i < len ; i++)
            strings[i] = strings[i].charAt(n) + strings[i];

        Arrays.sort(strings);
        String [] ans = new String[len];

        for (int i = 0 ; i < len ; i++)
            ans[i] = strings[i].substring(1);

        return ans;
    }

    public static void main(String [] args)
    {
        String [] strings = {"sun", "bed", "cat"};
        String [] strs = {"abcd", "abce", "cdx"};

        System.out.println(Arrays.toString(solution(strings, 1)));
        System.out.println(Arrays.toString(solution(strs, 2)));
    }
}
