package lessons.lesson08.Leader.Dominator;

import java.util.*;

class sjjyy
{
	 public static int solution(int [] A)
	 {
		 Stack <Integer> stack = new Stack<>();
		 int len = A.length;
		 
		 for (int i = 0 ; i < len ; i++)
		 {
			 if (stack.isEmpty())
				 stack.push(A[i]);
			 
			 if (stack.peek() == A[i])
				 stack.push(A[i]);
			 else
				 stack.pop();
		 }
		 
		 int res = -1;
		 int max_cnt = 0;
		 int max_num = -1;
		 
		if (stack.size() > 0)
			res = stack.peek();
		
		for(int j = 0 ; j < len ; j++)
		{
			if (res == A[j])
				max_cnt++;
			if (max_cnt > len/2)
			{
				max_num = j;
				break;
			}
		}

		return max_num;
	 }

	 
	public static void main(String[] args)
	{
		int A[] = {3, 4, 3, 2, 3, -1, 3, 3};
		System.out.println(solution(A));
	}

}
