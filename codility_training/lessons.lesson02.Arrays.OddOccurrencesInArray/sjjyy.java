package lessons.lesson02.Arrays.OddOccurrencesInArray;

public class sjjyy
{
    public static int solution(int[] A)
    {
         int a = 0;
        
        for (int i=0; i<A.length; i++)
            a ^= A[i];
                
        return a;
    }

    public static void main(String[] args)
    {
        int b[] = {9, 7, 9, 3, 7};
        
        System.out.println(solution(b));
    }
}
