package lessons.lesson07.StacksandQueues.Brackets;

import java.util.*;

class sjjyy
{
	 public static int solution(String S)
	 {
		 Stack<Character> stack = new Stack<>();
		 int len = S.length();
		    
		    for (int i = 0 ; i < len ; i++)
		    {
		        char c = S.charAt(i);
		        
		        if (stack.isEmpty())
	                return 0;
		        
		        if (c == '(' || c == '{' || c == '[')
		            stack.push(c);
		        
		        else
		        {           		            
		            char last = stack.pop();
		            
		            if (c == ')' && last != '(')
		                return 0;
		        		            
		            if (c == '}' && last != '{')
		                return 0;
		           		            
		            if (c == ']' && last != '[')
		                return 0;          
		        }
		    }
		    
		    if (!stack.isEmpty())
		        return 0;
		    		    
		    return 1;

		}

	 
	 	public static void main(String[] args)
	 	{
	 		String S = "{[[()(]]}";
	 		System.out.println(solution(S));
	 	}

}
