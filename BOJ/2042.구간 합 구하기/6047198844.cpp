#include <iostream>
#include <vector>
#define LL long long
using namespace std;

//https://www.acmicpc.net/board/view/38941
void change(int changed_idx, LL changing_num, vector<LL>& temp,vector<LL> &idx_tree) {
	LL dif = changing_num - temp[changed_idx];
	temp[changed_idx] = changing_num;
	int N = idx_tree.size() - 1;
	while (changed_idx <= N) {
		idx_tree[changed_idx] += dif;
		changed_idx += (changed_idx & -changed_idx);
	}
	return;
}

LL sum(int idx, vector<LL>& idx_tree) {
	LL res = 0;
	while (idx) {
		res += idx_tree[idx];
		idx -= idx & (-idx);
	}
	return res;
}

LL prefix_sum(int from_idx, int to_idx, vector<LL>& idx_tree) {
	return sum(to_idx,idx_tree) - sum(from_idx - 1,idx_tree);
}


int main() {
	int N, M, K;
	cin >> N >> M >> K;
	vector <LL> temp(N + 1);
	for (int i = 1; i <= N; i++)
		cin >> temp[i];

	vector <LL> idx_tree(N + 1);
	for (int i = 1; i <= N; i++)
		for (int j = i - (i & -i) + 1; j <= i; j++)
			idx_tree[i] += temp[j];

	int C = M + K;

	LL a, b, c;
	while (C--) {
		cin >> a >> b >> c;
		if (a == 1)
			change(b, c, temp, idx_tree);
		else
			cout << prefix_sum(b, c, idx_tree) << "\n";
	}
}