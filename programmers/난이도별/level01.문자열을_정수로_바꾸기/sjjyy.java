package 난이도별.level01.문자열을_정수로_바꾸기;

public class sjjyy
{
    public static int solution(String s)
    {
        return Integer.parseInt(s);
    }

    public static void main(String[] args)
    {
        System.out.println(solution("12435")); // 12435
        System.out.println(solution("+2314")); // 2314
        System.out.println(solution("-314")); // -314
    }
}
