#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//a와 b를 곱한값을 리턴한다.
vector <int> multiply(const vector<int>& a, const vector<int>& b) {
	int an = a.size();
	int bn = b.size();
	vector<int> res(an + bn + 1, 0);
	for (int i = 0; i < an; i++) {
		for (int j = 0; j < bn; j++) {
				res[i + j] += a[i] * b[j];
		}
	}
	return res;
}

//a가 항상 크다고 가정한다. a에서 b를 뺀다.
void subFrom(vector<int>& a, vector<int>& b) {
	int bn = b.size();
	for (int i = 0; i < bn; i++)
		a[i] -= b[i];
}

//a + b * (10^k)
void addTo(vector<int>& a, vector<int>& b, int k) {
	//vector<int> bm(k);
	//int bn = b.size();
	//for (int i = 0; i < bn; i++)
	//	bm.push_back(b[i]);

	//while (a.size() < bm.size())
	//	a.push_back(0);

	//for (int i = 0; i < bm.size(); i++)
	//	a[i] += bm[i];

	int length = b.size();
	a.resize(max(a.size(), b.size() + k));
	for (int i = 0; i < length; i++)
		a[i + k] += b[i];
}

vector<int> karatsuba(const vector<int>& a, const vector<int>& b) {
	int an = a.size();
	int bn = b.size();
	if (an < bn) karatsuba(b, a);
	if (an == 0 || bn == 0) return vector<int>();
	if (an <= 50) return multiply(a, b);
	int half = an / 2;
	vector<int> a0(a.begin(), a.begin() + half);
	vector<int> a1(a.begin() + half, a.end());

	vector<int> b0(b.begin(), b.begin() + min<int>(bn, half));
	vector<int> b1(b.begin() + min<int>(bn, half), b.end());

	vector<int> z0 = karatsuba(a1, b1);
	vector<int> z1 = karatsuba(a0, b0);
	addTo(a1, a0, 0);
	addTo(b1, b0, 0);
	vector<int> z2 = karatsuba(a1, b1);
	subFrom(z2, z0);
	subFrom(z2, z1);

	vector<int> res;
	addTo(res, z0, half + half);
	addTo(res, z2, half);
	addTo(res, z1, 0);
	return res;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		string A;
		string B;
		cin >> A >> B;

		int N = A.size();
		vector<int> group(N);
		for (int i = 0; i < N; i++)
			group[i] = (A[N - 1 - i] == 'M');

		int M = B.size();
		vector<int> fan(M);
		for (int i = B.size() - 1; i >= 0; i--)
			fan[i] = (B[i] == 'M');

		vector<int> res = karatsuba(group, fan);
		int cnt = 0;
		//맴버의수는 항상 팬의 수 이하이다.
		for (int i = N - 1; i < M; i++)
			if (!res[i])
				cnt++;
		cout << cnt << "\n";
	}
}