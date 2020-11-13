package 난이도별.level01.시저_암호;

import java.util.stream.Collectors;

public class sjjyy {
    public static String solution(String s, int n) {

        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isLowerCase(c))
                c = (char) ('a' + (c + n - 'a') % 26);

            else if (Character.isUpperCase(c))
                c = (char) ('A' + (c + n - 'A') % 26);

            ans.append(c);
        }

        return ans.toString();
    }

    public static String solution2(String s, int n)
    {
        return s.chars()
                .map(c -> Character.isUpperCase(c) ? (char) ('A' + (c + n - 'A') % 26) :
                        Character.isLowerCase(c) ? (char) ('a' + (c + n - 'a') % 26) : c)
                .mapToObj(c -> Character.toString((char) c))
                        .collect(Collectors.joining(""));
    }

    public static String solution3(String s, int n)
    {

        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            ans.append(
                    Character.isLowerCase(c) ? (char) ('a' + (c + n - 'a') % 26) :
                            Character.isUpperCase(c) ? (char) ('A' + (c + n - 'A') % 26) :
                                    c
            );
        }

        return ans.toString();
    }

    public static void main(String[] args)
    {
        System.out.println(solution("AB", 1)); // BC
        System.out.println(solution("z", 1)); // a
        System.out.println(solution("a B z", 4)); // e F d

        System.out.println(solution2("AB", 1)); // BC
        System.out.println(solution2("z", 1)); // a
        System.out.println(solution2("a B z", 4)); // e F d

        System.out.println(solution3("AB", 1)); // BC
        System.out.println(solution3("z", 1)); // a
        System.out.println(solution3("a B z", 4)); // e F d
    }
}
