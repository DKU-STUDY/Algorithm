package lessons.lesson04.CountingElements.MissingInteger;

import java.util.*;

class sjjyy
{
    public static int solution(int[] A)
    {
        Arrays.sort(A);
        int cnt = 1;
        int len = A.length;
        for(int i = 0; i < len; i++)
        {
            if(A[i] == cnt)
                cnt++;
        }
        
        return cnt;
    }
    
    public static void main(String[] args)
    {
        int[] A = new int[] {1, 3, 1, 4, 2, 3, 5, 4};
        int[] B = new int[] {1, 1, 4, 2, 5};
        System.out.println(solution(A));
        System.out.println(solution(B));
    }
    
}
