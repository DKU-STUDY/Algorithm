package lessons.lesson15.CaterpillarMethod.CountDistinctSlices;

public class sjjyy
{
    public static int solution(int M, int[] A) // performance 80%
    {
        int len = A.length;
        int [] appearence = new int[M+1];

        int front = 0;
        int back = 0;
        int result = 0;

        while(back < len)
        {
            while (front < len && appearence[A[front]] == 0)
            {
                appearence[A[front]] += 1;

                result += (front - back + 1);
                front += 1;
            }

            appearence[A[back]] = 0;
            back += 1;

            // if (result >= 1_000_000_000)
            //    return 1_000_000_000;

        }
        return Math.min(result, 1000000000);
    }


    public static void main(String[] args)
    {
        int M = 6;
        int[] A = {3, 4, 5, 5, 2};
        System.out.println(solution(M, A)); // 9
    }
}
