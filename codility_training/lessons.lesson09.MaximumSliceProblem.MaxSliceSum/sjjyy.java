package lessons.lesson09.MaximumSliceProblem.MaxSliceSum;

class sjjyy
{
	 public static int solution(int [] A)
	 {
	     int len = A.length;
	        
	     if(len == 1) return A[0];
	        
	     int max = 0;
	     // int maxSlice = 0;
	     int maxSlice = Integer.MIN_VALUE;
	        
	     for (int i = 0 ; i < len ; i++)
	     {
	         max = Math.max(A[i], A[i] + max);
	         maxSlice = Math.max(max, maxSlice);
	     }
	        
	     return maxSlice;
	 }


	public static void main(String[] args)
	{
		int A[] = {3, 2, -6, 4, 0};
		System.out.println(solution(A)); // 5
	}

}
