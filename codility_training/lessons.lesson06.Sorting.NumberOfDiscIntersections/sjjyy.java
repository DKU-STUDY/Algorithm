package lessons.lesson06.Sorting.NumberOfDiscIntersections;

import java.util.*;

public class sjjyy
{
    public static int solution(int [] A) // 어려워서 Mickey0521님 참고했습니다.
    {
        int len = A.length;

        long [] left = new long[len];
        long [] right = new long[len];

        int intersection = 0;

        for(int i = 0 ; i < len ; i++)
        {
            right[i] = i - (long) A[i];
            left[i] = i + (long) A[i];
        }

        Arrays.sort(left);
        Arrays.sort(right);

        int low = 0;

        for(int i = 0 ; i < len ; i++)
        {
            while (low < len && left[i] >= right[low])
            {
                intersection = intersection + low;
                intersection = intersection - i;
                low++;
            }
        }

        if(intersection > 10000000)
            return -1;

        return intersection;
    }

    public static void main(String[] args)
    {
        int [] A = {1, 5, 2, 1, 4, 0};
        System.out.println(solution(A)); // 11
    }
}
