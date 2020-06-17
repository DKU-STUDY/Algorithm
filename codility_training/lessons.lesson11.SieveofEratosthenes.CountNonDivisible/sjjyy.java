package lessons.lesson11.SieveofEratosthenes.CountNonDivisible;

// import java.util.ArrayList;
import java.util.Arrays;

public class sjjyy
{
    public static int[] solution(int[] A) // error
    {
        /*
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
        */

        int len = A.length;
        int max = A[0];
        for (int i = 1 ; i < len ; i++)
            max = Math.max(max, A[i]);

        int [] count = new int [max+1];

        for (int i = 0 ; i < len ; i++)
            count[A[i]]++;

        int [] nonDiv = new int [max+1];
        int len2 = nonDiv.length;

        for (int i = 1 ; i < len2 ; i++)
        {
            if (count[i] != 0)
                nonDiv[i] = len - count[i];
        }

        //sieve
        for (int i = 1 ; i < len2 ; i++)
        {
            if (count[i] != 0)
            {
                int s = i*2;
                while (s < len2)
                {
                    if (nonDiv[s] != 0)
                        nonDiv[s] -= count[i];

                    s+=i;
                }
            }
        }

        int [] result = new int [len];
        for (int i = 0 ; i < len ; i++)
        {
            result[i] = nonDiv[A[i]];
        }

        return result;
    }

    public static void main(String[] args)
    {
        int [] A = {3, 1, 2, 3, 6};
        System.out.println(Arrays.toString(solution(A))); // [2, 4, 3, 2, 0]
    }
}
