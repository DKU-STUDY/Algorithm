//�� ������ �����̴� �Ϸ翡 2���͸� ���ö󰥼��ִ�.
//���� ������ 1���͹ۿ� �ö��� ���Ѵ�.
//m�ϰ� �� ��¥�� �� �� Ȯ���� ��Ȯ�� 75%�̴�.
//m�� �ȿ� �����̰� �칰 ������ �ö� Ȯ����?
//climb(days, climbed) --> days���� climbed��ŭ �ö�����, m�Ͼȿ� n�̻� �ö� Ȯ��. �޸������̼��� ���ؼ� ������ ���ڸ� �ִ��� ���δ�.
//climb(days, climbed) = 0.75 * climb(days+1, climbed+2) + 0.25 * climb(days+1, climbed+1)
//�� �������� �񰡿�Ȯ���� 75% . ���� ���� Ȯ���� 25%�� ���Ѱ��� ���� ��ä Ȯ���̴�. --> ����� �������̴�.
#include <iostream>
#include <cstring>
#include <vector>

#define MAX_NUM 1000
using namespace std;

int n;
int m;

double climb(int days, int climbed, vector<vector<double>> &vt) {
	if (days == m) return climbed >= n ? 1 : 0;
	double &res = vt[days][climbed];
	if (res != -1)
		return res;
	return res = 0.75 * climb(days + 1, climbed + 2,vt) + 0.25 * climb(days + 1, climbed + 1,vt);
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		cin >> n >> m;
		vector<vector<double>> vt(MAX_NUM + 1, vector<double>(2 * MAX_NUM + 1, -1));
		cout.precision(11);
		cout << climb(0, 0,vt) << "\n";
	}
}
