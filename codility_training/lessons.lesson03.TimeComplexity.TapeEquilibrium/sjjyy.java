class Solution {
    public static int solution(int[] A) {
        
        int left = 0, right=0, result = 0, sum = 0;
        int len = A.length;
        
        for(int i = 0; i <= len ; i++)
            sum += A[i];
        
        for (int j = 1 ; j < len ; j++)
        {
            left += A[j-1];
            right = sum - left;
            result = Math.min(result, Math.abs(left-right));
        }
        return result;
    }
}
