package lessons.lesson07.StackandQueues.StoneWall;

import java.util.*;

class sjjyy
{
	 public static int solution(int[] H)
	 {
		 Stack<Integer> stack = new Stack<>();
		 int len = H.length;
		 int ans = 0;		 
		    
		    for (int i = 0 ; i < len ; i++)
		    {
		        if (stack.isEmpty() || stack.peek() < H[i])
		        {
		        	stack.push(H[i]);
		        	ans++;
		        }
		        else if (H[i] < stack.peek())
		        {
		        	stack.pop();
		        	i--;
		        }
		    }
		    
		    return ans;
		}

	 
	public static void main(String[] args)
	{
		int H[] = {8, 8, 5, 7, 9, 8, 7, 4, 8};
		System.out.println(solution(H)); // 7
	}

}
