package lessons.lesson03.TimeComplexity.FrogJmp;

class sjjyy
{
    public int solution(int X, int Y, int D)
    {
      return (Y-X) % D == 0 ? (Y-X) / D : (Y-X) / D + 1;
    }
    
    
    public static void main(String[] args) 
    {
  		System.out.println(solution(10, 85, 30));
  		System.out.println(solution(5, 100, 5));
	  	System.out.println(solution(20, 40, 30));
  	}
}
