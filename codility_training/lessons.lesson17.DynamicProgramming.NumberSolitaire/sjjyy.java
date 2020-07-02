package lessons.lesson17.DynamicProgramming.NumberSolitaire;

import java.util.Arrays;

public class sjjyy
{
    public static int solution(int[] A)
    {
        int len = A.length;
        int[] d = new int[len];
        Arrays.fill(d, Integer.MIN_VALUE);
        d[0] = A[0];

        for(int i = 0 ; i < len ; i++)
        {
            for(int j = i + 1 ; j < len && j < i+1 + 6 ; j++)
            {
                int k = d[j];
                int max = d[i] + A[j];
                d[j] = Math.max(k, max);
            }
        }

        return d[len-1];
    }

    public static int sol2(int[] A)
    {
        int len = A.length;
        int[] d = new int[len];


        return d[len-1];
    }

    public static void main(String[] args)
    {
        int[] A = {1, -2, 0, 9, -1, -2};
        System.out.println(solution(A)); // 8
        System.out.println(sol2(A)); // 8
    }
}
