package 난이도별.level01.자릿수_더하기;

public class sjjyy
{
    public static int solution(int n)
    {
        String num = String.valueOf(n);
        int len = num.length();
        int answer = 0;

        for (int i = 0 ; i < len ; i++)
            answer += Integer.parseInt(String.valueOf(num.charAt(i)));

        return answer;
        // return IntStream.range(0, len).map(i -> Integer.parseInt(String.valueOf(num.charAt(i)))).sum();
    }

    public static int solution2(int n)
    {
        int answer = 0;
        String[] arr = String.valueOf(n).split("");

        for (String s : arr)
            answer += Integer.parseInt(s);

        return answer;
        // return Arrays.stream(arr).mapToInt(Integer::parseInt).sum();
    }

    public static void main(String[] args)
    {
        System.out.println(solution(321)); // 6
        System.out.println(solution(1234567890)); // 45
        System.out.println(solution2(321)); // 6
        System.out.println(solution2(1234567890)); // 45
    }
}
