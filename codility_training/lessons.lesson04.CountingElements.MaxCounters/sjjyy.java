package lessons.lesson04.CountingElements.MaxCounters;

import java.util.*;

class sjjyy
{
	 public static int[] solution2(int N, int[] A)
	 {
			int tmp = 0;
			int fin = 0;
			int[] B = new int[N];
      
			int a = A.length, b = B.length;
					
			for (int k = 0; k < a; k++)
			{
				int n = A[k] - 1;
				if (1 <= A[k] && A[k] <= N)
				{
					B[n] = Math.max(B[n], fin);
					B[n] += 1;
					tmp = Math.max(tmp, B[n]);
				}
				else if (A[k] == N + 1)
					fin = tmp;
			}
			
			for(int i = 0 ; i < b; i++)
				B[i] = Math.max(B[i], fin);

			return B;
	 }

	 
	public static void main(String[] args)
	{
		int[] A = new int[] {3, 4, 4, 6, 1, 4, 4};
		System.out.println(Arrays.toString(solution(5, A)));
	}

}
