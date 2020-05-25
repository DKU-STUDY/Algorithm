package lessons.lesson07.StacksandQueues.Fish;

import java.util.*;

class sjjyy
{
	 public static int solution(int [] A, int [] B)
	 {
		 Stack<Integer> stack = new Stack<>();
		 int size, cnt = 0;
		 int len = A.length;
		 
		 for(int i = 0 ; i < len ; i++) 
		 {
			 if(B[i] == 1)
				 stack.push(A[i]);
			 else
			 {
			 while (!stack.isEmpty())
			 {
				 size = stack.peek();
				 
				 if (size > A[i])
					 break;
				 else
					 stack.pop();				 
			 }
			 if (stack.isEmpty())
				 cnt++;
			 }
		 }
		    	return cnt + stack.size();
	 }

	 
	public static void main(String[] args)
	{
		int A[] = {4, 3, 2, 1, 5};
		int B[] = {0, 1, 0, 0, 0};
		System.out.println(solution(A, B));
	}

}
