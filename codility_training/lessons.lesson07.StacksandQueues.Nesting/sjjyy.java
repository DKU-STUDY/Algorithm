// Brackets랑 무슨 차이인지 모르겠다...

package lessons.lesson07.StacksandQueues.Nesting;

import java.util.*;

class sjjyy
{
	 public static int solution(String S)
	 {
		 Stack<Character> stack = new Stack<>();
		 int len = S.length();
		 int ans = 0;		 
		    
		    for (int i = 0 ; i < len ; i++)
		    {
		    	char c = S.charAt(i);
		    	
		    	if (c =='(')
		    		stack.push('(');
		    	else if (stack.size() == 0 || stack.pop() != '(')
		    		return 0;
		    		
		    }
		    
		    return stack.size() == 0 ? 1 : 0;
		}

	 
	public static void main(String[] args)
	{
		String S = "((()))(";
		System.out.println(solution(S));
	}

}
