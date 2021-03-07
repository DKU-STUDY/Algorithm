//비가 내리면 달팽이는 하루에 2미터를 기어올라갈수있다.
//날이 맑으면 1미터밖에 올라가지 못한다.
//m일간 각 날짜에 비가 올 확률이 정확히 75%이다.
//m일 안에 달팽이가 우물 끝까지 올라갈 확률은?
//climb(days, climbed) --> days동안 climbed만큼 올라갔을때, m일안에 n이상 올라갈 확률. 메모이제이션을 위해서 과거의 인자를 최대한 줄인다.
//climb(days, climbed) = 0.75 * climb(days+1, climbed+2) + 0.25 * climb(days+1, climbed+1)
//즉 다음날에 비가올확률에 75% . 오지 않을 확률에 25%를 곱한것의 합이 전채 확률이다. --> 상당히 직관적이다.
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
