package 난이도별.level01.자릿수_더하기;


public class sjjyy
{
    public static int solution(int n)
    {
        int answer = 0;
        String num = String.valueOf(n);
        int len = num.length();

        for (int i = 0 ; i < len ; i++)
            answer += Integer.parseInt(String.valueOf(num.charAt(i)));

        return answer;
    }

    public static int solution2(int n)
    {
        int answer = 0;
        String[] arr = String.valueOf(n).split("");

        for (String s : arr)
            answer += Integer.parseInt(s);

        return answer;
    }

    public static void main(String[] args)
    {
        System.out.println(solution(321)); // 6
        System.out.println(solution(1234567890)); // 45
        System.out.println(solution2(321)); // 6
        System.out.println(solution2(1234567890)); // 45
    }
}
