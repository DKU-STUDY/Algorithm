package lessons.lesson09.MaximumSliceProblem.MaxDoubleSliceSum;

public class sjjyy
{

    public static int solution(int [] A)
    {
        int len = A.length;
        int[] L = new int[len];
        int[] R = new int[len];
        int max = 0;

        for(int i = 1 ; i < len ; i++)
            L[i] = Math.max(0, L[i-1]+A[i]); // A[X+1] + A[X+2] + ... + A[Y-1]

        for(int i = len - 2 ; i >= 0 ; i--)
            R[i] = Math.max(0, R[i+1] + A[i]); // A[Y+1] + A[Y+2] + ... + A[Z-1]

        for(int i = 1 ; i < len-1 ; i++)
            max = Math.max(max, L[i-1] + R[i+1]);

        return max;

    }

    public static void main(String[] args)
    {
        int [] A = {3, 2, 6, -1, 4, 5, -1, 2};
        System.out.println(solution(A)); // 17
    }
}
