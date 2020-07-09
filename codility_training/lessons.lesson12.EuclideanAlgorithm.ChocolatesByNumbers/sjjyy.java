package lessons.lesson12.EuclideanAlgorithm.ChocolatesByNumbers;

public class sjjyy
{
    public static int solution(int N, int M)
    {
       return N/(gcd(N,M));
    }

    public static int gcd(int a, int b) // using Uclidean algorithm
    {
    //    if(a % b == 0)
    //        return b;
    //    else
    //        return gcd(b, a % b);
        return a % b == 0 ? b : gcd(b, a % b);
    }

    public static void main(String[] args)
    {
        int N = 10;
        int M = 4;
        System.out.println(solution(N, M)); // 5
    }
}
