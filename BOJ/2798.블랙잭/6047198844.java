package algorithm.bruteforce;

import java.util.Scanner;
import java.util.Vector;

public class BOJ_2798_���� {
	//�迭 ũ��
	static int N;
	//�ִ�ġ
	static int M;
	
	//idx�� ����/�������� �ʾƼ� ������ִ� M�� ����� �ִ� ��
	static int brute_force(int sum, int idx, int remain, Vector <Integer> arr) {
		//������ ��� �Ϸ�Ȱ��
		if(remain==0&&sum<=M)
			return sum;
		//���ÿϷ���� ���� ���
		//���� ���ϴ� ���
		if(idx>=N||sum>M)
			return Integer.MIN_VALUE;
		int res = 0;
		//�����ϴ� ���
		res = brute_force(sum+arr.get(idx), idx+1, remain-1, arr);
		//���þ��ϴ� ���
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
