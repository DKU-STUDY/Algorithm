#include <iostream>
#include <queue>

using namespace std;

int main() {
	int T;
	cin >> T;
	while (T--) {
		int N, M;
		cin >> N >> M;
		priority_queue<int, vector<int>, less<int> > pq;
		queue<int> q;
		int cnt = 0;
			int _;
		for (int i = 0; i < N; i++) {
			cin >> _;
			pq.push(_);
			q.push(_);
		}
		while (!q.empty()) {

			if (pq.top() == q.front()) {
				++cnt;
				pq.pop();
				q.pop();
				if (M == 0) {
					cout << cnt << "\n";
					break;
				}
				else {
					M--;
				}

			}
			else {
				q.push(q.front());
				q.pop();
				if (M == 0)
					M = q.size() - 1;
				else
					M--;
			}
		}
	}
}