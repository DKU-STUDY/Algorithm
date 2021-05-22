#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N, M, K;
	cin >> N >> M;
	vector<vector<int>> A(N, vector<int>(M));
	for (int y = 0; y < N; y++)
		for (int x = 0; x < M; x++)
			cin >> A[y][x];

	cin >> M >> K;
	vector<vector<int>> B(M, vector<int>(K));
	for (int y = 0; y < M; y++)
		for (int x = 0; x < K; x++)
			cin >> B[y][x];

	for (int y = 0; y < N; y++) {
		for (int x = 0; x < K; x++) {
			int sum = 0;
			for (int z = 0; z < M; z++)
				sum += A[y][z] * B[z][x];
			cout << sum << " ";
		}
		cout << "\n";
	}

}

```