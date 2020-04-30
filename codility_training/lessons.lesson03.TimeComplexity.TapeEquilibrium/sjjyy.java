package lessons.lesson03.TimeComplexity.TapeEquilibrium;

class Solution
{
    public static int solution(int[] A)
    {
        
        int left = 0, right = 0, sum = 0;
        int result = Integer.MAX_VALUE; // 비교군으로 MAX값을 넣어야 min에서 최소값 도출 가능
        int len = A.length;
        
        for(int i = 0; i < len ; i++) // 수정
            sum += A[i];
        
        for (int j = 1 ; j < len ; j++)
        {
            left += A[j-1];
            right = sum - left;
            result = Math.min(result, Math.abs(left-right));
        }
        
        return result;
    }
    
    public static void main(String[] args)
    {
        int[] A = new int[] {2, 1, 3, 5, 4, 6};
        System.out.println(solution(A));
    }
    
}
