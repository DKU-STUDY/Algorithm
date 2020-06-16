package lessons.lesson11.SieveofEratosthenes.CountNonDivisible;

import java.util.ArrayList;

public class sjjyy
{
    public static int[] solution(int[] A) // error
    {
        int len = A.length;
        ArrayList<Integer> div = new ArrayList<Integer>();

        for(int i = 0 ; i < len ; i++)
             div.add(A[i]);

        int [] count = {};

        for (int i = 0 ; i < len ; i++)
        {
            int division = 0;

            for (int j = 1; j * j <= A[i] ; j++)
            {
                if(A[i] % j == 0)
                {
                    division += div.get(j);

                    if (A[i] / j != j)
                        division += div.get(A[i] / j);
                }
            }
            count[i] = len - division;
        }


        return count;
    }

    public static void main(String[] args)
    {
        int [] A = {3, 1, 2, 3, 6};
        System.out.println(solution(A)); // [2, 4, 3, 2, 0]
    }
}
