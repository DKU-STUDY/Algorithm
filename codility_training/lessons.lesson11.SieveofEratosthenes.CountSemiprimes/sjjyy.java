package lessons.lesson11.SieveofEratosthenes.CountSemiprimes;

import java.util.Arrays;
import java.util.stream.IntStream;

public class sjjyy
{
    public static int[] solution(int N, int[] P, int[] Q)
    {

        int len = P.length;
        int [] result = new int [len];
        int [] presum = new int [N+1];
        int [] flag = new int [N+1];

        flag[0] = 1;
        flag[1] = 1;

        for(int i = 2 ; i*i <= N ; i++) {
            if (flag[i] == 1)
                continue;

            int j = i * i;
            while (j <= N) {
                flag[j] = 1;
                j += i;
            }
        }

        for(int i = 2 ; i*i <= N ; i++) {
            if(flag[i] == 1)
                continue;

            int j = i * i;
            while (j <= N) {
                if (flag[i] == 0 && flag[j / i] == 0)
                    flag[j] = 2;

                j += i;
            }

        }

        int sem_prime_counter = 0;

        for(int i = 2 ; i <= N ; i++)
        {
            if(flag[i] == 2)
                sem_prime_counter++;
            presum[i] = sem_prime_counter;
        }

        for(int i = 0 ; i < len ; i++)
            result[i] = presum[Q[i]] - presum[P[i]-1];

        return result;
    }

    private static int [] seive(int N)
    {
        int [] seive = new int[N + 1];
        int i = 2;
        while (i * i <= N)
        {
            if(seive[i] == 0)
            {
                int j = i * i;
                while (j <= N)
                {
                    if(seive[j] == 0)
                        seive[j] = i;

                    j += i;
                }
            }
            i++;
        }
        int len = seive.length;
        int [] flags = new int[len];
        for(int k = 2 ; k < len ; k++)
        {
            if (seive[k] == 0)
                flags[k] = k;
            else
                flags[k] = seive[k];
        }
        return flags;
    }

    public static int[] solution2(int N, int[] P, int[] Q)
    {
        int [] flag = new int [N+1];
        int [] seive = seive(N);

        int len = flag.length;
        int Plen = P.length;

        for(int i = 4 ; i < len ; i++)
        {
            if (seive[i] * seive[i / seive[i]] == i) {
                flag[i] = 1;
            }
        }

        int[] preSum = new int[len];
        for (int i = 1; i < len; i++) {
            preSum[i] = preSum[i - 1] + flag[i];
        }

        int[] result = new int[Plen];
        for (int i = 0; i < Plen; i++) {
            result[i] = preSum[Q[i]] - preSum[P[i] - 1];
        }

        return result;
    }

    public static void main(String[] args)
    {
        int[] P = {1, 4, 16};
        int[] Q = {26, 10, 20};
        int N = 26;

        System.out.println(Arrays.toString(solution2(N, P, Q))); // [10, 4, 0]
    }
}
