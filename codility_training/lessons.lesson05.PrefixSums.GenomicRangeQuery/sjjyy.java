package lessons.lesson05.PrefixSums.GenomicRangeQuery;


class sjjyy
{
	// timeout error
	public static int[] solution2(String S, int[] P, int[] Q)
	{

		int len = P.length;
		int[] result = new int[len];
		
		for (int i = 0; i < len; i++)
		{
			String str = S.substring(P[i], Q[i] + 1);
			
			if (str.contains("A"))
				result[i] = 1;
			
			else if (str.contains("C"))
				result[i] = 2;
			
			else if (str.contains("G"))
				result[i] = 3;
			
			else if (str.contains("T"))
				result[i] = 4;
			
		}
		
		return result;

	}
	
	
 // 첫 코드가 timeout error로 나와서 다른 코드를 참고
	public static int[] solution(String S, int[] P, int[] Q)
	{
		int s_len = S.length();
		int p_len = P.length;
		int[][] arr = new int[s_len][4];
		int[] result = new int[p_len];

		for (int i = 0; i < s_len; i++)
		{
			char c = S.charAt(i);
			if (c == 'A')
				arr[i][0] = 1;
			if (c == 'C')
				arr[i][1] = 1;
			if (c == 'G')
				arr[i][2] = 1;
			if (c == 'T')
				arr[i][3] = 1;
		}

		for (int i = 1; i < s_len; i++)
		{
			for (int j = 0; j < 4; j++)
				arr[i][j] += arr[i - 1][j];
		}

		for (int i = 0; i < p_len; i++)
		{
			int x = P[i];
			int y = Q[i];

			for (int a = 0; a < 4; a++)
			{
				int sub = 0;
				if (x - 1 >= 0)
					sub = arr[x - 1][a];
				if (arr[y][a] - sub > 0) 
				{
					result[i] = a + 1;
					break;
				}
			}

		}
		return result;
	}

	public static void main(String[] args)
	{
		String S = "CAGCCTA";
		int[] P = { 2, 5, 0 };
		int[] Q = { 4, 5, 6 };

		int[] solution1 = solution(S, P, Q);

		for (int i : solution1)
			System.out.print(i + " ");
	}

}
