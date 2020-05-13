package lessons.lesson06.Sorting.MaxProductOfThree;

import java.util.*;

class sjjyy
{
	 public static int solution(int[] A)
	 {
		 int n = A.length - 1;
		 Arrays.sort(A);
		 
		 int ans1 = A[n] * A[n - 1] * A[n - 2];
		 int ans2 = A[0] * A[1] * A[n];
		 
		 return ans1 > ans2 ? ans1 : ans2;
	 }

	public static void main(String[] args)
	{
		int[] A = new int[] {2, 1, 1, 2, 3, 1};
		System.out.println(solution(A));
	}

}
