package 난이도별.level01.짝수와_홀수;

public class sjjyy {
    public static String solution(int num)
    {
        return num % 2 == 0 ? "Even" : "Odd";
    }

    public static void main(String[] args)
    {
        System.out.println(solution(3)); // Odd
        System.out.println(solution(4)); // Even
    }
}
