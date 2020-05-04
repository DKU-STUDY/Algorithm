package lessons.lesson04.CountingElements.PermCheck;

import java.util.*;

class sjjyy
{
    public static int solution(int[] A)
    {
        Arrays.sort(A);
        int len = A.length;
        for(int i = 0 ; i < len ; i++)
        {
            if(A[i] != i + 1)
                return 0;
        }
        
        return 1;
    }
    
    public static void main(String[] args)
    {
        int[] A = new int[] {1, 3, 1, 4, 2, 3, 5, 4};
        int[] B = new int[] {1, 4, 2, 3};
        System.out.println(solution(A));
        System.out.println(solution(B));
    }
    
}


// 
