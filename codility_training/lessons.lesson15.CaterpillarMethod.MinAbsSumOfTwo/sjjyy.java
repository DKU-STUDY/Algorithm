package lessons.lesson15.CaterpillarMethod.MinAbsSumOfTwo;

import java.util.Arrays;

public class sjjyy
{
    public static int solution(int[] A)
    {
        int len = A.length;
        Arrays.sort(A);

        int start = 0;
        int end = len - 1;
        int minAbsSum = Math.abs(A[start]+A[end]);

        while(start <= end)
        {
            int sum = A[start] + A[end];
            minAbsSum = Math.min(minAbsSum, Math.abs(sum));

            if(sum <= 0)
                start++;
            else
                end--;
        }
        return minAbsSum;
    }

    public static void main(String[] args)
    {
        int[] A = {-8, 4, 5, -10, 3};
        int[] B = {1, 4, -3};
        System.out.println(solution(A)); // 3
        System.out.println(solution(B)); // 1
    }
}
