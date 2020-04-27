class Solution {
    public int[] solution(int[] A, int K)
    {
        int len = A.length;
        int[] B = new int[len];
        
        for(int i = 0 ; i < len ; i++)
         B[(i+K) % len] = A[i];
        
        return B;
    }
}
