#include <iostream>
#include <queue>
using namespace std;



int max_length;
int end_stage;
int distance_w[102];
int cost[102];
int memo[102];
int memo_spot[102];
//지점 n에서 도착지점까지의 정비시간.
int dp(int n) {
	if (memo[n])
		return memo[n];
	if (n == end_stage)
		return 0;

	int res_min = 0;
	int cnt_distance = 0;
	for (int i = n + 1; i <= end_stage; i++) {
		cnt_distance += distance_w[i];
		if (cnt_distance > max_length)
			break;
		int temp = cost[n] + dp(i);
		if (!res_min || res_min > temp) {
			res_min = temp;
			memo_spot[n] = i;
		}
	}
	return memo[n] = res_min;
}

int main() {
	cin >> max_length;
	cin >> end_stage; end_stage++;
	distance_w[0] = 0;
	for (int i = 1; i <= end_stage; i++)
		cin >> distance_w[i];
	for (int i = 1; i < end_stage; i++)
		cin >> cost[i];
	cost[0] = cost[end_stage] = 0;
	cout << dp(0) << "\n";
	vector <int> vt;
	for (int i = memo_spot[0];i!= end_stage; i = memo_spot[i])
		vt.push_back(i);
	cout << vt.size() << "\n";
	for (int i : vt)
		cout << i << " ";
}