#include <iostream>
#include <vector>
using namespace std;

// A1과 A2의 곱셈
vector <vector<int>> multiplyMatrix(vector <vector<int>> A1, vector <vector<int>> A2) {
	int N = A1.size();
	vector <vector<int>> multiply_res;
	for (int y = 0; y < N; y++) {
		vector <int> temp;
		for (int x = 0; x < N; x++) {
			int element = 0;
			for (int a = 0; a < N; a++) {
				element += ((A1[y][a] % 1000) * (A2[a][x] % 1000)) % 1000;
				element %= 1000;
			}
			temp.push_back(element);
		}
		multiply_res.push_back(temp);
	}
	return multiply_res;
}

//중복연산 두번.
//문제조건
//자료형
vector <vector<int>> divide_and_conquer(vector <vector<int>> &A, long long B) {
	if (B == 1)
		return A;
	vector <vector<int>> temp = divide_and_conquer(A, B / 2);
	if (B % 2)
		return multiplyMatrix(multiplyMatrix(temp, temp), A);
	else
		return multiplyMatrix(temp, temp);
}


int main() {
	int N;
	cin >> N;
	long long B;
	cin >> B;
	vector <vector<int>> A;
	int num;
	for (int i = 0; i < N; i++) {
		vector <int> row;
		for (int j = 0; j < N; j++) {
			cin >> num;
			row.push_back(num);
		}
		A.push_back(row);
	}
	vector <vector<int>> res = divide_and_conquer(A, B);
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			cout << res[y][x] % 1000 << " ";
		}
		cout << "\n";
	}
}