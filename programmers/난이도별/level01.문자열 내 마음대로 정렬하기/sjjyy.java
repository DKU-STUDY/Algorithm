package 난이도별.level01.문자열_내_마음대로_정렬하기;

import java.util.*;

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

    public static String[] solution2(String[] strings, int n)
    {
        List<String> list = new ArrayList<>();

        for (String string : strings)
            list.add(string.charAt(n) + string);

        Collections.sort(list);
        String [] ans = new String[list.size()];

        for (int i = 0 ; i < list.size() ; i++)
            ans[i] = list.get(i).substring(1);

        return ans;
    }

    public static String[] solution3(String [] strings, int n)
    {
        return Arrays.stream(strings)
                .sorted(String::compareTo)
                .sorted(Comparator.comparingInt(a -> a.charAt(n)))
                .toArray(String[]::new);
    }

    public static void main(String [] args)
    {
        String [] strings = {"sun", "bed", "cat"};
        String [] strs = {"abcd", "abce", "cdx"};

//        System.out.println(Arrays.toString(solution(strings, 1)));
//        System.out.println(Arrays.toString(solution(strs, 2)));

//        System.out.println(Arrays.toString(solution2(strings, 1)));
//        System.out.println(Arrays.toString(solution2(strs, 2)));

        System.out.println(Arrays.toString(solution3(strings, 1)));
        System.out.println(Arrays.toString(solution3(strs, 2)));
    }
}
