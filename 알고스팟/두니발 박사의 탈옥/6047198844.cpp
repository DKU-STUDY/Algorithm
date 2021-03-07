#include <iostream>
#include <vector>
using namespace std;

double cache[51][101];

double findDuni(int here, int where,int remDay,vector<vector<int>> &road) {
	if (remDay == 0)
		return here == where;
	double& res = cache[here][remDay];
	if (res != 0)
		return res;

	int roadNum = road[here].size();
	double mul = 1 / (double)roadNum;
	for (int i = 0; i < roadNum; i++) {
		res += (mul) * findDuni(road[here][i], where, remDay - 1, road);
	}
	return res;
}

int main() {
	cout.precision(10);
	int c;
	cin >> c;
	while (c--) {
		//마을 , 지금까지 지난 일수, 교도소가 있는 마을의 번호
		int n, d, p;
		cin >> n >> d >> p;
		vector <vector<int>> road(n);
		int to_town;
		int from_town;
		int temp;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> temp;
				if (temp)
					road[i].push_back(j);
			}
		}
		int t;
		cin >> t;
		while (t--) {
			int q;
			cin >> q;
			for (int i = 0; i < n; i++)
				for (int j = 0; j <= d; j++)
					cache[i][j] = 0;
			cout << findDuni(p, q, d, road) << " ";
		}
		cout << "\n";
	}
}
