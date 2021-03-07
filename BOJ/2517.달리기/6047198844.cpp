#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

map <int, int> mp;
int N;

void update(int idx, vector<int>& res) {
	while (idx <= N) {
		res[idx] += 1;
		idx += idx & (-idx);
	}
	return;
}

int prefix_sum(int idx, vector<int>& res) {
	int sum = 0;
	while (idx > 0) {
		sum += res[idx];
		idx -= idx & (-idx);
	}
	return sum;
}

int main() {
	cin >> N;
	vector <int> index_tree_rank(N + 1);
	vector <int> temp(N + 1);
	vector <int> res(N + 1);

	for (int i = 1; i <= N; i++) {
		cin >> index_tree_rank[i];
		temp[i] = index_tree_rank[i];
	}
	sort(temp.begin(), temp.end());
	for (int i = 1; i <= N; i++)
		mp.insert({ temp[i],i });

	for (int i = 1; i <= N; i++) {
		update(mp[index_tree_rank[i]], res);
		cout << i - prefix_sum(mp[index_tree_rank[i]] - 1, res) << "\n";
	}
}
