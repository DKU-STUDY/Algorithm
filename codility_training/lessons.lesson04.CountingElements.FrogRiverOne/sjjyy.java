package lessons.lesson04.CountingElements.FrogRiverOne;

class Solution
{
    public static int solution(int X, int[] A)
    {      
        int[] set = new int[X];
        int leaf = 0, len = A.length;
        
        for (int i = 0 ; i < len ; i++)
        {
            int a = A[i];
            if (a <= X)
            {
               if(set[a-1] == 0)
               {
                   set[a-1] = 1;
                   leaf++;
               }
               
               if(leaf == X)
                   return i;
            }
        }
        
        if (leaf != X)
            return -1;
        
        return 0;
        
    }
    
    public static void main(String[] args)
    {
        int[] A = new int[] {1, 3, 1, 4, 2, 3, 5, 4};
        System.out.println(solution(4, A));
    }
    
}
