/*
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 
최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

ACAYKP
CAPCAK

*/

#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>
#include <cstring>

using namespace std;

int memo[1001][1001];

string a;
string b;


int LCS(int a_index, int b_index) {
	if (a_index == -1 || b_index == -1)
		return 0;

	int& ret = memo[a_index][b_index];
	if (ret!=-1)
		return ret;

	if (a[a_index] == b[b_index]) {
		return ret = 1 + LCS(a_index - 1, b_index - 1);
	}
	else {
		return ret = max(LCS(a_index, b_index -1), LCS(a_index-1, b_index));
	}
}

int main() {
	memset(memo, -1, sizeof(memo));
	cin >> a >> b;
	cout << LCS(a.size() - 1, b.size() - 1);
}