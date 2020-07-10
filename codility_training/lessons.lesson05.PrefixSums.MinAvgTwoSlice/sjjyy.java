package lessons.lesson05.PrefixSums.MinAvgTwoSlice;

public class sjjyy
{
    public static int solution(int[] A)
    {
        int len = A.length;
        double min = (A[0] + A[1]) / 2.0;
        int index = 0;

        // 평균은 a+...+b/n로 계산하며, a+b/2에서 a<=b이면 평균은 a보다 크거나 같다.
        // 따라서 a+b+c+d/4인 경우 (a+b)+(c+d)의 평균은 (a+b)<=(c+d)일 때 (a+b) 이상이 된다.
        // 문제에서 최소 원소 개수가 2개 이상이므로 2개와 3개인 그룹만 비교하면 된다.

        for(int i = 2 ; i < len ; i++)
        {
            if((A[i-1] + A[i]) / 2.0 < min)
            {
                min = (A[i-1] + A[i]) / 2.0;
                index = i-1;
            }

            if((A[i-2] + A[i-1] + A[i]) / 3.0 < min)
            {
                min = (A[i-2] + A[i-1] + A[i]) / 3.0;
                index = i-2;
            }
        }

        return index;

    }

    public static void main(String[] args)
    {
        int [] A ={4, 2, 2, 5, 1, 5, 8};

        System.out.println(solution(A));
    }
}
