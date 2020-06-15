package lessons.lesson12.EuclideanAlgorithm.CommonPrimeDivisors;

public class sjjyy
{
    public static int solution(int[] A, int[] B)
    {
        int len = A.length;
        int count = 0;

        for(int i = 0 ; i < len ; i++)
        {
            if(prime(A[i], B[i]))
                count++;
        }

        return count;
    }

    public static int gcd(int a, int b) // using Uclidean algorithm
    {
        return a % b == 0 ? b : gcd(b, a % b);
    }

    public static boolean prime(int a, int b)
    {
        int g = gcd(a, b);
        int gcd_A = 0, gcd_B = 0;

        while (gcd_A != 1)
        {
            gcd_A = gcd(a, g);
            a = a / gcd_A;
        }

        while (gcd_B != 1)
        {
            gcd_B = gcd(b, g);
            b = b / gcd_B;
        }

        return a == 1 && b == 1;
    }

    public static void main(String[] args)
    {
        int[] A = {15, 10, 3};
        int[] B = {75, 30, 5};
        System.out.println(solution(A, B)); // 1
    }
}
