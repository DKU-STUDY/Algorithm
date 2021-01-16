// *2 / +1 / -1
#include <iostream>
#include <queue>

using namespace std;

bool check[100001];
int num[100001];

int bfs(int N, int K) {
	queue <int> spot;
	spot.push(N);
	check[N] = true;
	while (!spot.empty()) {
		int node = spot.front();
		if (node == K)
			return num[K];
		spot.pop();
		if (node * 2 <= 100000 && (!check[node * 2]||num[node*2]>num[node])) {
			spot.push(node * 2);
			check[node * 2] = true;
			num[node * 2] = num[node];
		}
		if (node + 1 <= 100000 && (!check[node + 1] || num[node + 1] > num[node] + 1)) {
			spot.push(node + 1);
			check[node + 1] = true;
			num[node + 1] = num[node] + 1;
		}
		if (node - 1 >= 0 && (!check[node - 1] || num[node - 1] > num[node] + 1)) {
			spot.push(node - 1);
			check[node - 1] = true;
			num[node - 1] = num[node] + 1;
		}
	}
}

int main() {
	int N; 
	int K;
	cin >> N >> K;
	cout << bfs(N, K);
}