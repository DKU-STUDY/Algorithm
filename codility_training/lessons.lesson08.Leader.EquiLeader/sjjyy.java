package lessons.lesson08.Leader.EquiLeader;

import java.util.*;

class sjjyy
{
	 public static int solution(int [] A)
	 {
		 Stack <Integer> stack = new Stack<>();
		 int len = A.length;

		 for (int i = 0 ; i < len ; i++)
		 {
			 if (stack.isEmpty() || stack.peek() == A[i])
				 stack.push(A[i]);
			 else
				 stack.pop();
		 }

		int res = stack.size() > 0 ? stack.peek() : -1;
		int cnt = 0;
		
		for(int j = 0 ; j < len ; j++)
		{
			if (A[j] == res)
				cnt++;
		}
				
		if (cnt <= len/2)
			return 0;
		
		int leader = res;
		int leftCount = 0;
		int rightCount = 0;
		
		for (int i = 0 ; i < len ; i++)
		{
			if (A[i] == leader)
				rightCount++;
			
			if (rightCount > (i+1)/2 && (cnt-rightCount) > (len-i-1)/2)
				leftCount++;
		}
		
		return leftCount;
	 }


	public static void main(String[] args)
	{
		int A[] = {4, 3, 4, 4, 4, 2};
		System.out.println(solution(A));
	}

}
