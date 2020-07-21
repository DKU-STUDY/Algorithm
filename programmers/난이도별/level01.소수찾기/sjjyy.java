package 난이도별.level01.소수찾기;

public class sjjyy
{
    public static int solution(int n) // 75.0 / 100.0
    {
        int ans = 0;

        for (int i = 2 ; i <= n ; i++)
        {
            boolean isPrime = true;

            for (int j = 2 ; j*j <= i ; j++)
            {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
                ans++;
        }

        return ans;
    }

    public static void main(String [] args)
    {
        System.out.println(solution(10));
    }
}