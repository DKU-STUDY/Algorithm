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
        }

        return 0;
    }

    public static void main(String[] args)
    {
        int [] A = {1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2};
        System.out.println(solution(A)); // 3
    }
}
