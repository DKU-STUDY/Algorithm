package 난이도별.level01.최대공약수와_최소공배수;

import java.util.Arrays;

public class sjjyy
{
    public static int[] solution(int n, int m)
    {
        int[] answer = new int[2];

        int tmp;

        if (n < m)
        {
            tmp = m;
            m = n;
            n = tmp;
        }

        for (int i = 1; i < n; i++)
        {
            if (n % i == 0 && m % i == 0)
            {
                answer[0] = i;
                answer[1] = (n * m) / i;
            }
        }
        return answer;
    }

    public static void main(String[] args)
    {
        System.out.println(Arrays.toString(solution(3, 12))); // [3, 12]
        System.out.println(Arrays.toString(solution(2, 5))); // [1, 10]
    }
}
