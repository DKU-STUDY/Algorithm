package lessons.lesson05.PrefixSums.CountDiv;

class sjjyy
{
    public static int solution(int A, int B, int K) // 수학적으로 접근
    {
        return (B / K) - (A / K) + (A % K == 0 ? 1 : 0);
    }
    
    public static int solution0(int A, int B, int K) // 문제 그대로만 풀었을 때
    {
        int c = 0;
        
        for (int i = A ; i <= B ; i++)
        {
            if (i % K == 0) c++;
        }
        
        return c;
    }
    
    public static void main(String[] args)
    {
        System.out.println(solution(1, 5, 3));
        System.out.println(solution(6, 11, 2));
    }
    
}
