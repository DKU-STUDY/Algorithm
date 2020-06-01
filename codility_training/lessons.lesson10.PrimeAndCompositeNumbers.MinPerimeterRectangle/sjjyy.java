package lessons.lesson10.PrimeAndCompositeNumbers.MinPerimeterRectangle;


class sjjyy
{
	 public static int solution(int N)
	 {
		int a = 0, b = 0;
		int min = 0;
		int len = (int)Math.sqrt(N);
		
		for(int i = 1 ; i <= len ; i++)
		{
			if(N % i == 0)
			    a = i;
		}
		
		b = N/a;
		min = (a + b) * 2;
		
		return min;
		
	 }


	public static void main(String[] args)
	{
		int N = 30;
		System.out.println(solution(N)); // 22
	}

}
