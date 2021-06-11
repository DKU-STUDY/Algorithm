package Reverse_Integer;

public class SeokBin {
	//정수 범위를 넘어가는 int 다루는 법 주의!
	public int reverse(int x) {
		//결과로 나갈 변수
		int reversed = 0;
		//일의 자리를 뽑아낼 변수
		int pop;
		
		while(x != 0) {
			pop = x % 10; //1의 자리를 뽑아내기 위해 % 사용!!!
			x /= 10;
			//이전값 * 10 하고 1의자리 채우기
			//  -2147483648 <= reversed <= 2147483647!! 일의 자리 비교조건 주의!
			if(reversed>Integer.MAX_VALUE/10 || 
					reversed==Integer.MAX_VALUE/10 && pop > 7) {
				return 0;
			}
			if(reversed<Integer.MIN_VALUE/10 || 
					reversed==Integer.MIN_VALUE/10 && pop < -8) {
				return 0;
			}
			reversed =(reversed * 10) + pop;
		}
		 
	 return reversed;
	}
}
