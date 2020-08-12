package 난이도별.level01.정수_제곱근_판별;

public class sjjyy
{
    public static long solution(long n)
    {
        double sqrt = Math.sqrt(n);

        return sqrt == (int) sqrt ? (long)Math.pow(sqrt+1, 2) : -1;
    }

    public static void main(String[] args)
    {
        System.out.println(solution(121)); // 144
        System.out.println(solution(3)); // -1
    }
}
