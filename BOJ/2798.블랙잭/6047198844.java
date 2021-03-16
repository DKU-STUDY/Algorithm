package algorithm.bruteforce;

import java.util.Scanner;
import java.util.Vector;

public class BOJ_2798_블랙잭 {
	//배열 크기
	static int N;
	//최대치
	static int M;
	
	//idx를 선택/선택하지 않아서 만들수있는 M과 가까운 최대 수
	static int brute_force(int sum, int idx, int remain, Vector <Integer> arr) {
		//선택이 모두 완료된경우
		if(remain==0&&sum<=M)
			return sum;
		//선택완료되지 않은 경우
		//선택 못하는 경우
		if(idx>=N||sum>M)
			return Integer.MIN_VALUE;
		int res = 0;
		//선택하는 경우
		res = brute_force(sum+arr.get(idx), idx+1, remain-1, arr);
		//선택안하는 경우
		res = Math.max(res, brute_force(sum, idx+1, remain, arr));
		return res;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		Vector <Integer> arr = new Vector(N);
		for(int i = 0 ; i < N; i++) {
			int e = sc.nextInt();
			arr.add(e);	
		}
		System.out.println(brute_force(0,0,3,arr));
	}
}
