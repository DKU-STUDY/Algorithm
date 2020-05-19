package lessons.lesson06.Sorting.Triangle;

import java.util.*;

class sjjyy
{

   public static int solution(int[] A)
	 {
		 int n = A.length;
		 Arrays.sort(A);
		 
		for (int i = 0 ; i < n - 2 ; i++)
		{
			if (A[i + 1] > A[i + 2] - A[i])
				return 1;
		}
		
		 return 0;
	 }


	 public static int solution2(int[] A) // overflow
	 {
		 int n = A.length;
		 Arrays.sort(A);
		 
		for (int i = 0 ; i < n - 2 ; i++)
		{
			if (A[i] + A[i + 1] > A[i + 2])
				return 1;
		}
		
		 return 0;
	 }
   

	public static void main(String[] args)
	{
		int[] A = new int[] {2, 1, 1, 2, 3, 1};
		System.out.println(solution(A));
		System.out.println(solution2(A));
	}

}
