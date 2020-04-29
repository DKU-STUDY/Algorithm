package lessons.lesson03.TimeComplexity.permMissingElem;

class sjjyy
{
    public static int solution(int[] A)
    {      
        int len = A.length;
        int a = 0, b = 0;
        
        for(int i = 1 ; i <= len + 1 ; i++)
            a += i;
        
        for(int j = 0 ; j < len ; j++)
            b += A[j];
            
        return a - b;
    }
    
    public static void main(String[] args)
    {
        int[] A = new int[] {2, 1, 3, 5};
        System.out.println(solution(A));
    }
    
}
