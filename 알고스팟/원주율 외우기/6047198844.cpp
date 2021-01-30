//(주의: 이 문제는 TopCoder 의 번역 문제입니다.)
//
//가끔 TV 에 보면 원주율을 몇만 자리까지 줄줄 외우는 신동들이 등장하곤 합니다.이들이 이 수를 외우기 위해 사용하는 방법 중 하나로, 숫자를 몇 자리 이상 끊어 외우는 것이 있습니다.이들은 숫자를 세 자리에서 다섯 자리까지로 끊어서 외우는데, 가능하면 55555 나 123 같이 외우기 쉬운 조각들이 많이 등장하는 방법을 택하곤 합니다.
//
//이 때, 각 조각들의 난이도는 다음과 같이 정해집니다 :
//
//모든 숫자가 같을 때(예 : 333, 5555) 난이도 : 1
//숫자가 1씩 단조 증가하거나 단조 감소할 때(예 : 23456, 3210) 난이도 : 2
//두 개의 숫자가 번갈아 가며 출현할 때(예 : 323, 54545) 난이도 : 4
//숫자가 등차 수열을 이룰 때(예 : 147, 8642) 난이도 : 5
//그 외의 경우 난이도 : 10
//원주율의 일부가 입력으로 주어질 때, 난이도의 합을 최소화하도록 숫자들을 3자리에서 5자리까지 끊어 읽고 싶습니다.최소의 난이도를 계산하는 프로그램을 작성하세요.
//입력
//5
//12341234
//11111222
//12122222
//22222222
//12673939
//
//출력
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
	//모든 숫자가 같을때
	bool flag = false;
	for (int i = 0; i < n && !flag; i++) {
		if (s[0] != s[i])
			flag = true;
	}
	if (!flag)
		return 1;
	//flag = true;
	//단조증가
	for (int i = 1; i < n && flag; i++) {
		if (s[i] != s[i - 1] + 1)
			flag = false;
	}
	if (flag)
		return 2;
	//flag = false;
	//단조감소
	for (int i = 1; i < n && !flag; i++) {
		if (s[i] != s[i - 1] - 1)
			flag = true;
	}
	if (!flag)
		return 2;

	//두개의 숫자가 번갈아가며 나타날때
	//flag == true;
	for (int i = 2; i < n&&flag; i++) {
		if (s[i] != s[i % 2])
			flag = false;
	}
	if (flag)
		return 4;

	//숫자가 등차수열을 이룰떄
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

	for (int i = 3; i <= 5; i++)
		res = min(res, check(s.substr(idx, i)) + dp(idx + i, n, s, m));
	return res;
}

int main() {
	int C;
	cin >> C;
	cin.ignore();
	while (C--) {
		//자연수 하나하나 받는법
		string s;
		getline(cin, s);
		int n = s.length();
		vector <int> m(n, -1);
		cout << dp(0, n, s, m) << "\n";
	}
}