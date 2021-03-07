#include <iostream>
#include <vector>
#define LL vector<long long>

using namespace std;
vector <LL> vt({ LL({1,1}),LL({1,0}) });

vector <LL> multiply_matrix(vector <LL> A, vector <LL> B) {
	vector <LL> res({
		LL({
			(A[0][0] % 1000000007 * B[0][0] % 1000000007 + A[0][1] % 1000000007 * B[1][0] % 1000000007) % 1000000007,
			(A[0][0] % 1000000007 * B[0][1] % 1000000007 + A[0][1] % 1000000007 * B[1][1] % 1000000007) % 1000000007}),
		LL({
			(A[1][0] % 1000000007 * B[0][0] % 1000000007 + A[1][1] % 1000000007 * B[1][0] % 1000000007) % 1000000007,
			(A[1][0] % 1000000007 * B[0][1] % 1000000007 + A[1][1] % 1000000007 * B[1][1] % 1000000007) % 1000000007}) });
	return res;
}

vector <LL> divide_and_conquer(long long n) {
	if (n == 1)
		return vt;
	vector <LL> res = divide_and_conquer(n / 2);
	vector <LL> square_res = multiply_matrix(res, res);
	//n이 2로 안나누어질때, 홀수일때
	if (n % 2)
		return multiply_matrix(square_res, vt);
	return square_res;
}

int main() {
	long long n;
	cin >> n;
	if (n == 0) {
		cout << "0";
		return 0;
	}
	vector <LL> res = divide_and_conquer(n);
	cout << res[0][1] % 1000000007;
}