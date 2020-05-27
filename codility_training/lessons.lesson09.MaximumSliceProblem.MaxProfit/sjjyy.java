package lessons.lesson09.MaximumSliceProblem.MaxProfit;


class sjjyy
{
	 public static int solution(int [] A)
	 {
	     int len = A.length;
	     int max = Integer.MIN_VALUE;
	     int min = Integer.MAX_VALUE;
		 
	     if (len == 0 || len == 1)
	    	 return 0;
	     	     
	     for (int i = 0 ; i < len ; i++)
	     {
	    	 min = Math.min(A[i], min);
	    	 max = Math.max(max, A[i]-min);
	     }
		 return max;
	 }


	public static void main(String[] args)
	{
		int A[] = {23171, 21011, 21123, 21366, 21013, 21367};
		System.out.println(solution(A)); // 356
	}

}
