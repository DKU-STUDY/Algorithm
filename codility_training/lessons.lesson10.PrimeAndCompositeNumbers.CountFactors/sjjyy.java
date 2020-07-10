package lessons.lesson10.PrimeAndCompositeNumbers.CountFactors;

class sjjyy
{
	 public static int solution(int N)
	 {
		int result = 0;
		double sqrt = Math.sqrt(N);
		
		for (int i = 1 ; i <= sqrt ; i++)
		{
			if (N % i == 0)
				result++;
		}
		
		result = result * 2; // pair
		
		if (sqrt * sqrt == N)
			result--;
		
		return result;
	 }


	public static void main(String[] args)
	{
		int N = 24;
		System.out.println(solution(N)); // 8
	}

}
