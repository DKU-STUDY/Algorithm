package lessons.lesson15.CaterpillarMethod.CountDistinctSlices;

public class sjjyy
{
    public static int solution(int M, int[] A)
    {
        int len = A.length;
        boolean [] appearence = new boolean[M+1];

        int front = 0;
        int back = 0;
        int result = 0;

        while(back < len)
        {
            while (front < len && !appearence[A[front]])
            {
                appearence[A[front]] = true;

                result += (front - back + 1);
                front += 1;

                if (result >= 1000000000)
                    return 1000000000;
            }

            appearence[A[back]] = false;
            back += 1;

        }

        return result;
    }


    public static void main(String[] args)
    {
        int M = 6;
        int[] A = {3, 4, 5, 5, 2};
        System.out.println(solution(M, A)); // 9
    }
}
