package lessons.lesson06.Sorting.Distinct;

import java.util.Set;
import java.util.HashSet;

class sjjyy
{
	 public static int solution(int[] A)
	 {
		 Set<Integer> hs = new HashSet<>();
		 int len = A.length;
		 
		 for (int i = 0; i < len ; i++)
			 hs.add(A[i]);
		 
		 return hs.size();
		
	 }

	public static void main(String[] args)
	{
		int[] A = new int[] {2, 1, 1, 2, 3, 1};
		System.out.println(solution(A));
	}

}
