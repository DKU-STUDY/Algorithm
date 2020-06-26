package lessons.lesson15.CaterpillarMethod.CountTriangles;

import java.util.Arrays;

public class sjjyy
{
    public static int solution(int[] A)
    {
        int len = A.length;
        Arrays.sort(A);
        int result = 0;

        for(int i = 0 ; i < len - 2 ; i++)
        {
            int left = i+1;
            int right = i+2;

            while (left<len-1)
            {
                if(right < len && A[i] + A[left] > A[right])
                    right++;
                else
                {
                    result += right - left - 1;
                    left++;
                }
            }
        }

        return result;
    }

    public static void main(String[] args)
    {
        int[] A = {10, 2, 5, 1, 8, 12};
        System.out.println(solution(A)); // 4
    }
}
