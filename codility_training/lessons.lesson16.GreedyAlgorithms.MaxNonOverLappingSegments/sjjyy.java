package lessons.lesson16.GreedyAlgorithms.MaxNonOverLappingSegments;

public class sjjyy
{
    public static int solution(int[] A, int[] B)
    {
        int len = A.length;

        int count = 1;
        int end = B[0];

        if(len <= 1)
           return len;

        for(int i = 1 ; i < len ; i++)
        {
            if(A[i] > end) // 첫 끝점 < 다음 시작점
            {
                count++;
                end = B[i];
            }
        }

        return count;

    }

    public static void main(String[] args)
    {
        int[] A = {1, 3, 7, 9, 9};
        int[] B = {5, 6, 8, 9, 10};
        System.out.println(solution(A, B)); // 3
    }
}
