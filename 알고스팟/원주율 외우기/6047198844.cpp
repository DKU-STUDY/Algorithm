//(����: �� ������ TopCoder �� ���� �����Դϴ�.)
//
//���� TV �� ���� �������� � �ڸ����� ���� �ܿ�� �ŵ����� �����ϰ� �մϴ�.�̵��� �� ���� �ܿ�� ���� ����ϴ� ��� �� �ϳ���, ���ڸ� �� �ڸ� �̻� ���� �ܿ�� ���� �ֽ��ϴ�.�̵��� ���ڸ� �� �ڸ����� �ټ� �ڸ������� ��� �ܿ�µ�, �����ϸ� 55555 �� 123 ���� �ܿ�� ���� �������� ���� �����ϴ� ����� ���ϰ� �մϴ�.
//
//�� ��, �� �������� ���̵��� ������ ���� �������ϴ� :
//
//��� ���ڰ� ���� ��(�� : 333, 5555) ���̵� : 1
//���ڰ� 1�� ���� �����ϰų� ���� ������ ��(�� : 23456, 3210) ���̵� : 2
//�� ���� ���ڰ� ������ ���� ������ ��(�� : 323, 54545) ���̵� : 4
//���ڰ� ���� ������ �̷� ��(�� : 147, 8642) ���̵� : 5
//�� ���� ��� ���̵� : 10
//�������� �Ϻΰ� �Է����� �־��� ��, ���̵��� ���� �ּ�ȭ�ϵ��� ���ڵ��� 3�ڸ����� 5�ڸ����� ���� �а� �ͽ��ϴ�.�ּ��� ���̵��� ����ϴ� ���α׷��� �ۼ��ϼ���.
//�Է�
//5
//12341234
//11111222
//12122222
//22222222
//12673939
//
//���
//4
//2
//5
//2
//14

#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm>

#define INF 1000000

using namespace std;

int check(string s) {
	int n = s.length();
	//��� ���ڰ� ������
	bool flag = false;
	for (int i = 0; i < n && !flag; i++) {
		if (s[0] != s[i])
			flag = true;
	}
	if (!flag)
		return 1;
	//flag = true;
	//��������
	for (int i = 1; i < n && flag; i++) {
		if (s[i] != s[i - 1] + 1)
			flag = false;
	}
	if (flag)
		return 2;
	//flag = false;
	//��������
	for (int i = 1; i < n && !flag; i++) {
		if (s[i] != s[i - 1] - 1)
			flag = true;
	}
	if (!flag)
		return 2;

	//�ΰ��� ���ڰ� �����ư��� ��Ÿ����
	//flag == true;
	for (int i = 2; i < n&&flag; i++) {
		if (s[i] != s[i % 2])
			flag = false;
	}
	if (flag)
		return 4;

	//���ڰ� ���������� �̷ꋚ
	//flag == false
	for (int i = 1; i < n && !flag; i++) {
		if (s[i] - s[i - 1] != s[1] - s[0])
			flag = true;
	}
	if (!flag)
		return 5;
	return 10;
}


int dp(int idx, int n ,string& s, vector <int>& m) {
	int &res = m[idx];
	if (res != -1)
		return res;
	int remain_lth = n - idx;
	if (remain_lth < 3)
		return INF;
	else if (remain_lth == 3 || remain_lth == 4 || remain_lth == 5)
		return res = check(s.substr(idx));
	res = INF;
	for (int i = 3; i <= 5; i++)
		res = min(res, check(s.substr(idx, i)) + dp(idx + i, n, s, m));
	return res;
}

int main() {
	int C;
	cin >> C;
	cin.ignore();
	while (C--) {
		//�ڿ��� �ϳ��ϳ� �޴¹�
		string s;
		getline(cin, s);
		int n = s.length();
		vector <int> m(n, -1);
		cout << dp(0, n, s, m) << "\n";
	}
}
