#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int cache[500][500];
int page[500];

//����i���� ����j������ ������ "��������" �߻��ϴ� ���
int dp(int i, int j) {
	//��ĥ�������� -> �� 0�� ����� �߻��Ѵ�, ��ĥ��������.
	if (i == j)
		return 0;
	int& res = cache[i][j];
	if (res != -1)
		return res;

	int sum = 0;
	//i���� j���� ����� ���� ������ �� ����Ѵ�. �̶� sum�� dp(i,k)�� dp(k+1,j)�� ���������� ��� ����̴�.
	for (int k = i; k <= j; k++)
		sum += page[k];

	int tmp;
	for (int k = i; k+1 <= j; k++) {
		tmp = (dp(i, k) + dp(k + 1, j) + sum);
		if (res == -1 || tmp < res)
			res = tmp;
	}
	return res;
}
int main() {
	int T, K, temp;
	cin >> T;
	while (T--) {
		memset(cache, -1, sizeof(cache));
		memset(page, 0, sizeof(page));
		cin >> K;
		for (int i = 0; i < K; i++)
			cin >> page[i];
		cout << dp(0, K - 1) << "\n";
	}
}
