package lessons.lesson05.PrefixSums.PassingCars;


class sjjyy
{
	 public static int solution(int[] A)
	 {
		 int result = 0;
		 int count = 0;
		 int len = A.length;
		 
		 for (int i = 0; i < len ; i++)
		 {
			 if (A[i] == 0)
				 count++;
			 else
				 result += count;
		 }
		 
		 if (result > 1000000000)
			 return -1;
		 
		return result;
		
	 }

	public static void main(String[] args)
	{
		int[] A = new int[] {0, 1, 0, 1, 1};
		System.out.println(solution(A));
	}

}
