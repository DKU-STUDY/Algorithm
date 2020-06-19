package lessons.lesson13.FibonacciNumbers.Ladder;

import java.util.Arrays;

public class sjjyy
{
    public static int [] solution(int [] A, int [] B)
    {
        int len = A.length;
        double max1 = Math.pow(2, 30);
        // int max = (int) max1;

        int max = Integer.parseInt(String.valueOf(Math.round(max1)));

        int [] P = new int[len+2];
        P[1] = 1; P[2] = 2;

        for (int i = 3 ; i < len+1 ; i++)
            P[i] = (P[i-1] + P[i-2]) % max;

        int [] c = new int[len];
        for(int i = 0 ; i < len ; i++) {
            // div 2^B[i]
            c[i] = P[A[i]] % (int) Math.pow(2, B[i]);
        }

        return c;
    }

    public static void main(String [] args)
    {
        int [] A = {4, 4, 5, 5, 1};
        int [] B = {3, 2, 4, 3, 1};
        System.out.println(Arrays.toString(solution(A, B))); // [5, 1, 8, 0, 1]
    }
}