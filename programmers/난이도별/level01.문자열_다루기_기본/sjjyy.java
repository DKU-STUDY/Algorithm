package 난이도별.level01.문자열_다루기_기본;

public class sjjyy {
    public static boolean solution(String s)
    {
        int len = s.length();

        if (len == 4 || len == 6)
        {
            try {
                Integer.parseInt(s); // 문자열 -> 정수
                return true;
            } catch (NumberFormatException e) { // 숫자 형식 오류
                return false;
            }
        }

        return false;
    }

    public static boolean solution2(String s)
    {
        int len = s.length();

        if (len == 4 || len == 6)
            return s.matches("[0-9]+");

        return false;

    }

    public static void main(String[] args)
    {
        System.out.println(solution("1234")); // true
        System.out.println(solution("s123")); // false

        System.out.println(solution2("1234")); // true
        System.out.println(solution2("s123")); // false
        System.out.println(solution2("4323s2")); // false
    }
}
