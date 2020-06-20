package lessons.lesson10.PrimeAndCompositeNumbers.Peaks;

import java.util.ArrayList;

public class sjjyy
{
    public static int solution(int[] A)
    {
        int len = A.length;
        ArrayList<Integer> peaks = new ArrayList<>();

        for(int i = 1 ; i < len-1 ; i++)
        {
            if(A[i-1] < A[i] && A[i+1] < A[i])
                peaks.add(i);
        }

        if(peaks.size() <= 1)
            return peaks.size();

        for(int num = len ; num >= 1 ; num--)
        {
           // 1st method
           if (len % num == 0)
            {
                int size = len / num;
                int block = 0;

                for(int j : peaks)
                {
                    if(j / size == block)
                        block++;
                }

                if(block == num)
                    return num;
            }

           /* 2nd method - time-out error
            if (len % num != 0) continue;

            int size = len / num;
            int block = peaks.stream()
                    .reduce(0, (n, j) -> n + (j / size == n ? 1 : 0));

            if(block == num) return num;
            */
        }

        return 0;
    }

    public static void main(String[] args)
    {
        int [] A = {1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2};
        int [] B = {1, 3, 2, 1};
        int [] C = {0, 1, 0, 0, 0};
        System.out.println(solution(A)); // 3
        System.out.println(solution(B)); // 1
        System.out.println(solution(C)); // 1
    }
}
