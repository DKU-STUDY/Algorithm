package lessons.lesson13.FibonacciNumbers.FibFrog;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class sjjyy
{
    public static int solution(int[] A) // 83%
    {
        int aLen = A.length;
        List<Integer> jmp = new ArrayList<>();
        jmp.add(1);
        jmp.add(1);

        int next = 0;

        while (next < aLen -1)
        {
            next = jmp.get(jmp.size()-1) + jmp.get(jmp.size()-2);
            jmp.add(next);
        } // fibonacci

        int[] min = new int[aLen + 2];

        Arrays.fill(min, Integer.MAX_VALUE);
        min[0] = 0;
        int mLen = min.length;

        for(int i = 0 ; i < mLen ; i++)
        {
            if(i == 0 || i == mLen - 1 || A[i-1] == 1)
            {
                for(int j : jmp)
                {
                    if(j > i)
                        break;
                    min[i] = (int) Math.min(min[i], (long) min[i-j]+1);
                }
            }
        }

        if(min[mLen-1] == Integer.MAX_VALUE)
            return -1;

        return min[mLen-1];
    }

    public static int solution2(int[] A) // modify
    {
        int aLen = A.length;
        if(aLen == 0) return 1;

        List<Integer> jmp = new ArrayList<>();
        jmp.add(1);
        jmp.add(1);

        int next = 2;

        return 0;
    }

    public static void main(String[] args)
    {
        int[] A = {0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0};
        System.out.println(solution(A)); // 3
        System.out.println(solution2(A)); // 3
    }
}
