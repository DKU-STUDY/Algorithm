package lessons.lesson16.GreedyAlgorithms.TieRopes;

public class sjjyy
{
    public static int solution(int K, int[] A)
    {
        int len = 0;
        int result = 0;

        for(int rope : A)
        {
            len += rope;

            if (len >= K)
            {
                result++;
                len = 0;
            }
        }
        return result;
    }

    public static void main(String[] args)
    {
        int K = 4;
        int[] A = {1, 2, 3, 4, 1, 1, 3};
        System.out.println(solution(K, A));
    }
}
